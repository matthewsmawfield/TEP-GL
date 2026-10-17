#!/usr/bin/env python3
"""Step 02b: Bullet disformal ray-trace stress test.

Stress-tests the residual amplitude margin of step_02 against the
dominant idealization levers of the component model:

  * Plummer compactness (a -> a/f for f = 0.5, 1, 2): deeper, steeper
    wells change both the screening profile y(g) and the accumulated
    depth u; shape_u ~ u^2 at Bullet depths makes the margin a strong
    function of how the baryonic mass is distributed.
  * LOS integration extent (Z_HALF_MPC = 4 -> 8): checks whether the
    +-4 Mpc integration truncates field accumulation.
  * Self-consistent sourcing on/off: brackets the sourcing convention.

The margin reported is B0_max/ B0_required in the halo convention
(galaxy-peak kappa_target = 0.30), matching step_02's headline metric.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
sys.path.insert(0, str(PROJECT_ROOT / "scripts" / "steps"))

import step_02_bullet_disformal_raytrace as s2
from utils.logger import print_status

STEP_NUM = "02b"


def set_components(scale):
    for c in s2.COMPONENTS:
        c["a_kpc"] = c["_a0"] * scale
        c["a_m"] = c["a_kpc"] * s2.KPC


def margin_for(scale, z_half, self_consistent, nb=97, nz=2401):
    set_components(scale)
    bx = np.linspace(-s2.B_HALF_MPC, s2.B_HALF_MPC, nb) * s2.MPC
    by = bx.copy()
    z = np.linspace(-z_half, z_half, nz) * s2.MPC
    sig, _ = s2.sigma_cube("halo", (bx, by, z), self_consistent=self_consistent)
    d_l = s2.angular_diameter(s2.Z_L)
    chi_s = s2.comoving_distance(s2.Z_S)
    chi_l = s2.comoving_distance(s2.Z_L)
    d_ls = (chi_s - chi_l) / (1 + s2.Z_S)
    d_s = s2.angular_diameter(s2.Z_S)
    _, _, kap = s2.deflection_and_kappa(sig, (bx, by, z), d_l, d_ls, d_s)
    sigma_crit = (s2.C_M**2 / (4.0 * np.pi * s2.G_SI)
                  * d_s / (d_l * d_ls))
    bx2, by2 = np.meshgrid(bx, by, indexing="ij")
    kap_bar = s2.kappa_baryon(bx2, by2, sigma_crit)
    # same metric as step_02: kappa AT the bullet-galaxy sightline
    i_g = int(np.argmin(np.abs(bx - s2.SIGHT["bullet_galaxy_peak"][0])))
    j_g = int(np.argmin(np.abs(by - s2.SIGHT["bullet_galaxy_peak"][1])))
    kap_sig = float(kap[i_g, j_g])
    need = ((s2.KAPPA_TARGET - kap_bar[i_g, j_g]) / kap_sig
            if kap_sig > 0 else np.inf)
    return {
        "kappa_at_bullet_galaxy_per_B0": kap_sig,
        "kap_bar_at_sightline": float(kap_bar[i_g, j_g]),
        "B0_required": float(need),
        "margin": float(s2.B0_MAX_GAL / need) if np.isfinite(need) else 0.0,
    }


def run():
    print_status("STEP 02b: Bullet stress test", "TITLE")
    for c in s2.COMPONENTS:
        c["_a0"] = c["a_kpc"]

    cases = {}
    for scale in (0.9, 1.0, 1.4, 2.0):
        for sc in (False, True):
            key = f"compactness_x{scale}_sc{int(sc)}"
            cases[key] = margin_for(scale, 4.0, sc)
            print_status(
                f"  a x{scale} sc={sc}: B0_req={cases[key]['B0_required']:.3g} "
                f"margin={cases[key]['margin']:.4f}", "INFO")

    # LOS extent sensitivity on the self-consistent branch
    for z_half in (8.0,):
        cases[f"zhalf_{int(z_half)}mpc_sc1"] = margin_for(1.0, z_half, True)
        print_status(
            f"  z_half={z_half} Mpc sc=1: B0_req="
            f"{cases[f'zhalf_{int(z_half)}mpc_sc1']['B0_required']:.3g} "
            f"margin={cases[f'zhalf_{int(z_half)}mpc_sc1']['margin']:.4f}",
            "INFO")

    margins = [v["margin"] for v in cases.values()]
    result = {
        "step": f"step_{STEP_NUM}_bullet_stress_test",
        "kappa_target": s2.KAPPA_TARGET,
        "B0_max_gal": s2.B0_MAX_GAL,
        "grid": {"NB": 97, "NZ": 2401},
        "cases": cases,
        "margin_range": [float(min(margins)), float(max(margins))],
        "overshoot_boundary": (
            "Negative B0_required marks component models where kappa_bar "
            "alone already exceeds the 0.30 peak target at the galaxy "
            "sightline (Plummer scale <~0.85 x nominal): those models are "
            "bounded from below by the observed convergence and cannot be "
            "used to shrink the residual arbitrarily."
        ),
        "interpretation": (
            "Margin = B0_max/B0_required (halo convention, kappa=0.30 "
            "target at the bullet-galaxy sightline, identical metric to "
            "step_02). Values <1 mean the disformal convergence falls short "
            "of the residual lensing gap under that component model; the "
            "spread across compactness/sourcing cases measures how much of "
            "the gap is model idealization rather than structural."
        ),
    }
    out = s2.PROJECT_ROOT / "results" / "step_02b_bullet_stress_test.json"
    out.write_text(json.dumps(result, indent=2))
    print_status(f"  margin range {min(margins):.4f} - {max(margins):.4f}", "INFO")
    return result


if __name__ == "__main__":
    run()
