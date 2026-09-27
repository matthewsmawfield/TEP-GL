#!/usr/bin/env python3
"""
Step 01: Temporal-Composite amplitude ledger (Issue 4-4 bookkeeping).

Computes the source-dependent Temporal-Composite response on the two
physically distinct carriers used in the manuscript, and the amplitude each
proposed discriminator actually probes:

  (a) Chronometric envelope -- the clock-transfer map of Box 3.1 evaluated
      as a delay field (Delta-tau ~ 3 yr over an Einstein-radius scale).
      This is an inference-space (reconstruction) amplitude: for photons the
      conformal sector contributes exactly zero differential transport
      (null-cone invariance; Paper 19 step_56 conformal residual = 0.0 d).

  (b) Propagating carrier -- the disformal multipath deformation bounded by
      GW170817 to |c_gamma - c_g|/c <= 1e-15, i.e. Delta T <= 0.2 s over the
      2 Mpc halo path. This is the only sector producing a genuine
      image-plane delay for photons (the paper's Regime-I scale).

Also corrects the source proper motion used in Box 3.2: v_s = 1000 km/s at
D_A = 1 Gpc gives mu_s = 2.1e-7 arcsec/yr (0.2 uas/yr), not 2e-4 arcsec/yr.

Outputs: results/step_01_amplitude_ledger.json
"""

import json
import math
import os

# --- units -----------------------------------------------------------------
C = 299792.458            # km/s
S_PER_YR = 3.15576e7
PC_KM = 3.085677581e13
ARCSEC_PER_RAD = 206264.806247

# --- inputs (as quoted in the manuscript) -----------------------------------
v_s_kms = 1000.0          # cluster transverse source velocity (Box 3.2)
D_A_Gpc = 1.0             # angular-diameter distance (Box 3.2)
L_halo_Mpc = 2.0          # effective halo path depth (Box 3.1)
grad_dtau_env_yr_per_arcsec = 3.0   # yr-scale clock-transfer map over ~arcsec
gw_bound = 1e-15          # |c_gamma - c_g|/c (Section 4, GW170817)
mu_mag = 10.0             # representative magnification near critical curve
flux_anomaly = (0.10, 0.30)         # Einstein Cross anomaly scale
nudot_frac_per_month = 0.10         # quasar fractional variability, active phase
sigma_shape2 = 0.09                 # weak-lensing shape-noise variance (~0.3^2)
s8_tension_frac = 0.05              # ~5% S8 tension scale
dt_fermat_d = 100.0                 # fiducial inter-image delay, days

# --- source proper motion ----------------------------------------------------
v_pc_per_yr = v_s_kms * S_PER_YR / PC_KM          # 1.02e-3 pc/yr
D_A_pc = D_A_Gpc * 1e9
mu_s_rad_per_yr = v_pc_per_yr / D_A_pc            # 1.02e-12 rad/yr
mu_s_arcsec_per_yr = mu_s_rad_per_yr * ARCSEC_PER_RAD   # ~2.1e-7
mu_s_uas_per_yr = mu_s_arcsec_per_yr * 1e6               # ~0.21

# --- Temporal-Composite shear amplitude -------------------------------------
# gamma_TC = mu_s * d(theta) Delta T_eff  (eq:gl_tc_jacobian norm)

# (a) chronometric envelope (inference-space field, Box 3.1 scale)
gamma_env = mu_s_arcsec_per_yr * grad_dtau_env_yr_per_arcsec          # ~6e-7

# (b) propagating disformal carrier (GW170817-saturated)
lighttime_halo_s = L_halo_Mpc * 1e6 * PC_KM * 1e3 / (C * 1e3)           # 2.06e14 s
lighttime_halo_yr = lighttime_halo_s / S_PER_YR                        # 6.5e6 yr
dT_prop_s = gw_bound * lighttime_halo_s                                # ~0.21 s
dT_prop_yr = dT_prop_s / S_PER_YR                                      # ~6.5e-9 yr
gamma_prop = mu_s_arcsec_per_yr * dT_prop_yr                           # ~1.4e-15

# --- per-test probed amplitudes ----------------------------------------------
# (i) Einstein Cross (Box 5.2)
dmu_over_mu_jac_env = mu_mag * gamma_env            # Jacobian route
dmu_over_mu_jac_prop = mu_mag * gamma_prop
nudot_per_yr = nudot_frac_per_month * 12.0          # fractional rate per yr
dF_env = nudot_per_yr * 3.0                          # emission-time route, 3 yr
dF_prop = nudot_per_yr * dT_prop_yr                  # ~1e-8
# archival flux-ratio precision ~1% bounds coherent emission-time contrast:
dt_em_bound_d = 0.01 / nudot_per_yr * 365.25         # ~3 days

# (ii) S8 covariance (Box 5.3): relative covariance term gamma_TC^2 / sigma_sh^2
cov_frac_env = gamma_env**2 / sigma_shape2
cov_frac_prop = gamma_prop**2 / sigma_shape2
# gamma_TC needed for a 5% bias of the shear *covariance* (order unity of the
# cosmic-shear power, sigma_cosmic ~ 0.03 RMS): gamma_needed^2 ~ s8_tension_frac
# x sigma_cosmic^2 is over-conservative; use the transparent bound instead:
#   relative correction to any two-point statistic <= gamma_TC^2 / sigma_shape2
gamma_needed_s8 = math.sqrt(s8_tension_frac * sigma_shape2)  # shear-noise level
                                                              # needed if the
                                                              # extra variance
                                                              # were to equal
                                                              # 5% of shape
                                                              # noise

# (iii) variability-mass correlation (Box 3.3): delta_kappa ~ gamma_TC
dM_spec = 0.10                       # proposed 10% mass precision
dM_needed_env = gamma_env            # ~6e-7
dM_needed_prop = gamma_prop          # ~1e-14
# delay-absorption route: a propagating residual dT absorbed into the model
# shifts the inferred mass/time-delay distance by ~dT/dt_Fermat
dT_absorption_bound_d = dM_spec * dt_fermat_d      # ~10 d at 10% precision

# (iv) shear-variability spec (<0.5% scatter) bounds gamma_TC < 5e-3:
gamma_scatter_spec = 5e-3
grad_bound_yr_per_arcsec = gamma_scatter_spec / mu_s_arcsec_per_yr

# (v) lens-model closure bound (existing data): propagating inter-image
# residuals larger than ~10% of the Fermat delay would already violate
# successful lens modeling -> dT <= ~10 d for 100 d delays.

# --- standard-physics baseline for the kinematics correlation -----------------
# The Temporal-Composite Jacobian dA^TC = -mu_s . grad(Delta T_eff) is sourced
# by ANY emission-time map, including the ordinary GR Fermat/Shapiro surface:
# a moving source's effective source-plane position is beta - mu_s DeltaT under
# standard physics as well. The kinematics-correlated shear-variance signature
# is therefore shared with particle-DM + GR at the standard-map level; the
# TEP-discriminating content is the residual above this computable baseline.
# Fiducial gradient: a ~100 d inter-image delay across a ~2 arcsec quad
# separation -> ~0.14 yr/arcsec. For galaxy-galaxy lensing (day-scale delay
# gradients over ~arcsec) the baseline is ~1e-3 yr/arcsec.
dtheta_quad_arcsec = 2.0
grad_fermat_yr_per_arcsec = (dt_fermat_d / 365.25) / dtheta_quad_arcsec
gamma_std_strong = mu_s_arcsec_per_yr * grad_fermat_yr_per_arcsec
dtheta_weak_arcsec = 1.0
dt_weak_d = 1.0
gamma_std_weak = mu_s_arcsec_per_yr * (dt_weak_d / 365.25) / dtheta_weak_arcsec

# --- conformal-sector cancellation audit (Issue 4-1) -------------------------
# Two equivalent statements fix the photon content of the clock-transfer map:
#   (i)  null-cone invariance: A^2 g(k,k)=0 iff g(k,k)=0, so coordinate transit
#        along a fixed spatial path is identical in g_tilde and g;
#   (ii) the Temporal Shear Sigma = grad ln A is an exact one-form, hence its
#        open-path integral is endpoint-determined and cancels between any two
#        rays sharing endpoints.
# Statement (ii) is verified numerically on the toy halo profile of Box 3.1 by
# trapezoidal integration along two piecewise rays with different pericenters
# sharing one source and one observer. The scalar-amplitude integral
# int(A-1)dl is evaluated on the same paths to show that the reconstruction
# field is genuinely path-dependent (the chronometric envelope) while
# propagating nothing.

eps_halo = 1e-6          # toy coupling (Box 3.1)
r0_kpc = 10.0            # characteristic scale (Box 3.1)
KPC_PER_MPC = 1e3


def lnA(x, y):
    r = math.hypot(x, y)
    return math.log1p(eps_halo * math.log(r / r0_kpc))


def A_minus_1(x, y):
    r = math.hypot(x, y)
    return eps_halo * math.log(r / r0_kpc)


def path_integral(p0, p1, p2, func, n=200000):
    """Trapezoidal integral of func(x,y)*dl along the two legs p0->p1->p2,
    p0 = source (kpc), p1 = lens-plane crossing point (kpc), p2 = observer."""
    total = 0.0
    for a, b in ((p0, p1), (p1, p2)):
        ax, ay = a
        bx, by = b
        seg = math.hypot(bx - ax, by - ay)
        h = seg / n
        s = 0.5 * (func(ax, ay) + func(bx, by))
        for i in range(1, n):
            t = i / n
            s += func(ax + (bx - ax) * t, ay + (by - ay) * t)
        total += s * h
    return total


def one_form_integral(p0, p1, p2, n=200000):
    """Integral of the exact shear one-form grad(ln A).dl along p0->p1->p2.
    grad lnA = eps/(1+eps ln(r/r0)) * (x,y)/r^2; integrand per unit parameter
    t is grad lnA . (b-a)."""
    total = 0.0
    for a, b in ((p0, p1), (p1, p2)):
        ax, ay = a
        tx, ty = b[0] - ax, b[1] - ay
        s = 0.0
        for i in range(n + 1):
            t = i / n
            x = ax + tx * t
            y = ay + ty * t
            r2 = x * x + y * y
            val = eps_halo / (1.0 + eps_halo * math.log(math.sqrt(r2) / r0_kpc)) \
                * (x * tx + y * ty) / r2
            w = 0.5 if i in (0, n) else 1.0
            s += w * val
        total += s / n
    return total


# endpoints (kpc): lens at origin; source and observer slightly asymmetric so
# that the endpoint-determined value is itself nonzero.
source = (-1500.0, 0.0)
observer = (1000.0, 0.0)
ray_inner = (source, (0.0, 5.0), observer)    # pericenter ~5 kpc
ray_outer = (source, (0.0, 50.0), observer)   # pericenter ~50 kpc

# numerical verification: the shear one-form integrates to the same
# endpoint-determined value on both rays.
int_lnA_ray1 = one_form_integral(*ray_inner)
int_lnA_ray2 = one_form_integral(*ray_outer)
int_lnA_exact = lnA(*observer) - lnA(*source)
d_sigma_path = int_lnA_ray1 - int_lnA_ray2          # ~0 up to quadrature error
resid_ray1 = int_lnA_ray1 - int_lnA_exact
resid_ray2 = int_lnA_ray2 - int_lnA_exact

int_Am1_ray1 = path_integral(*ray_inner, A_minus_1)          # kpc
int_Am1_ray2 = path_integral(*ray_outer, A_minus_1)
d_Am1_kpc = int_Am1_ray2 - int_Am1_ray1
d_Am1_s = d_Am1_kpc * PC_KM * 1e3 / C               # s
d_Am1_yr = d_Am1_s / S_PER_YR

ledger = {
    "step": "01",
    "status": "success",
    "description": "Temporal-Composite amplitude ledger: corrected proper "
                   "motion, propagating-carrier (disformal, GW170817-bounded) "
                   "vs chronometric-envelope (inference-space) amplitudes, and "
                   "the delay-field amplitude each discriminator probes.",
    "corrections": {
        "mu_s_manuscript_arcsec_per_yr": 2e-4,
        "mu_s_correct_arcsec_per_yr": mu_s_arcsec_per_yr,
        "mu_s_correct_uas_per_yr": mu_s_uas_per_yr,
        "unit_slip_factor": 2e-4 / mu_s_arcsec_per_yr,
        "note": "0.2 uas/yr was printed as 2e-4 arcsec/yr (mas/uas slip); "
                "the envelope gamma_TC is 6e-7, not 6e-4.",
    },
    "carriers": {
        "conformal_sector_audit": {
            "exact_one_form_integral_inner_ray": int_lnA_ray1,
            "exact_one_form_integral_outer_ray": int_lnA_ray2,
            "endpoint_value_lnAobs_minus_lnAsrc": int_lnA_exact,
            "quadrature_residual_inner": resid_ray1,
            "quadrature_residual_outer": resid_ray2,
            "multipath_differential_shear_integral": d_sigma_path,
            "scalar_field_integral_inner_ray_kpc": int_Am1_ray1,
            "scalar_field_integral_outer_ray_kpc": int_Am1_ray2,
            "scalar_field_integral_contrast_yr": d_Am1_yr,
            "photon_differential_residual_d": 0.0,
            "cross_check": "Paper 19 step_56 conformal_only_additional_residual_days = 0.0",
            "interpretation": "the shear one-form is exact: verified to "
                              "quadrature precision on the Box-3.1 toy halo "
                              "for two rays of different pericenter sharing "
                              "one source and observer, its open-path "
                              "integral is endpoint-determined and its "
                              "multipath differential vanishes; the scalar "
                              "amplitude integral int(A-1)dl is genuinely "
                              "path-dependent but is a timelike-congruence "
                              "clock-transfer field (chronometric envelope), "
                              "not a photon delay",
        },
        "chronometric_envelope": {
            "dT_yr_per_arcsec": grad_dtau_env_yr_per_arcsec,
            "gamma_TC": gamma_env,
            "interpretation": "reconstruction-space clock-transfer map; "
                              "zero differential photon transport "
                              "(null-cone invariance; Paper 19 step_56 = 0.0 d)",
        },
        "propagating_disformal": {
            "gw_bound_fractional": gw_bound,
            "lighttime_halo_yr": lighttime_halo_yr,
            "dT_s_per_halo": dT_prop_s,
            "gamma_TC": gamma_prop,
            "interpretation": "Regime-I ms-s channel; the only propagating "
                              "image-plane delay for photons",
        },
        "standard_baseline": {
            "mechanism": "the same mu_s . grad(DeltaT) structure is generated "
                         "by the ordinary GR Fermat/Shapiro surface: under "
                         "particle DM + GR a moving source's effective "
                         "source-plane position is beta - mu_s DeltaT",
            "grad_fermat_yr_per_arcsec_quad": grad_fermat_yr_per_arcsec,
            "gamma_std_strong_lens": gamma_std_strong,
            "gamma_std_galaxy_galaxy": gamma_std_weak,
            "envelope_over_std_strong": gamma_env / gamma_std_strong,
            "propagating_over_std_strong": gamma_prop / gamma_std_strong,
            "interpretation": "existence of kinematics-correlated shear "
                              "variance is shared with standard physics at "
                              "~1e-8 (strong lenses) to ~1e-9 (galaxy-galaxy); "
                              "TEP-discriminating content is the residual "
                              "over this computable baseline -- the "
                              "propagating disformal piece sits ~7 orders "
                              "below it (timing-tested, not shear-tested), "
                              "and the chronometric envelope is "
                              "reconstruction-space (bound-set only)",
        },
    },
    "discriminators": {
        "lensed_frb_residual": {
            "probes": "dT directly",
            "threshold": "<0.1 ms achromatic ensemble residual",
            "powered_for": "propagating carrier (ms-s); flagship test",
        },
        "einstein_cross_flux": {
            "jacobian_route_dmu_over_mu_env": dmu_over_mu_jac_env,
            "jacobian_route_dmu_over_mu_prop": dmu_over_mu_jac_prop,
            "emission_route_dF_over_F_env": dF_env,
            "emission_route_dF_over_F_prop": dF_prop,
            "required_anomaly": list(flux_anomaly),
            "shortfall_env": flux_anomaly[0] / dmu_over_mu_jac_env,
            "archival_emission_bound_d": dt_em_bound_d,
            "verdict": "10-30% anomalies are microlensing terrain, not "
                       "claimed by TEP at propagating amplitude; ~1% archival "
                       "photometry bounds coherent emission-time contrast at "
                       "~3 d and the yr-scale reading overshoots (dF/F~3) -- "
                       "the test is a bound-setting correlation program",
        },
        "s8_covariance": {
            "cov_frac_env": cov_frac_env,
            "cov_frac_prop": cov_frac_prop,
            "gamma_needed_for_5pct_of_shape": gamma_needed_s8,
            "verdict": "relative covariance ~4e-12 even at the envelope: the "
                       "TC term cannot source the ~5% S8 tension; retained "
                       "prediction is existence of source-class covariance",
        },
        "variability_mass": {
            "dM_needed_env": dM_needed_env,
            "dM_needed_prop": dM_needed_prop,
            "spec_precision": dM_spec,
            "delay_absorption_bound_d": dT_absorption_bound_d,
            "verdict": "10% mass precision is ~1e5 above the envelope TC "
                       "response; the same precision bounds any propagating "
                       "delay at <=10 d per 100 d delay, already excluding "
                       "a propagating yr-scale residual (consistent with "
                       "the conformal null)",
        },
        "shear_variability": {
            "gamma_bound_at_spec": gamma_scatter_spec,
            "grad_bound_yr_per_arcsec": grad_bound_yr_per_arcsec,
            "verdict": "weak direct bound on the delay gradient; reaching "
                       "the envelope requires ~1e-5 fractional scatter "
                       "precision",
        },
        "lens_model_closure": {
            "bound": "propagating dT <= ~10% of Fermat delay (~10 d per 100 d)",
            "verdict": "existing strong-lens model closure excludes "
                       "propagating year-scale residuals outright",
        },
    },
}

out = os.path.join(
    os.path.dirname(__file__), "..", "..", "results",
    "step_01_amplitude_ledger.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    json.dump(ledger, f, indent=2)

print(json.dumps({k: v for k, v in ledger.items()
                  if k in ("corrections", "carriers")}, indent=2))
print("wrote", os.path.normpath(out))
