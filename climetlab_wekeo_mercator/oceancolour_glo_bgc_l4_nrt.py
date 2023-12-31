#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_mercator.main import Main

LAYERS = [
    "cmems_obs-oc_glo_bgc-optics_nrt_l4-multi-4km_P1M_202207",  # noqa: E501 Cmems obs-oc glo bgc-optics NRT l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-gapfree-multi-4km_P1D_202207",  # noqa: E501 Cmems obs-oc glo bgc-plankton NRT l4-gapfree-multi-4km p1d
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-multi-4km_P1M_202207",  # noqa: E501 Cmems obs-oc glo bgc-plankton NRT l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-300m_P1M_202211",  # noqa: E501 Cmems obs-oc glo bgc-plankton NRT l4-olci-300m p1m
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-4km_P1M_202207",  # noqa: E501 Cmems obs-oc glo bgc-plankton NRT l4-olci-4km p1m
    "cmems_obs-oc_glo_bgc-pp_nrt_l4-multi-4km_P1M_202207",  # noqa: E501 Cmems obs-oc glo bgc-pp NRT l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-multi-4km_P1M_202207",  # noqa: E501 Cmems obs-oc glo bgc-reflectance NRT l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-300m_P1M_202211",  # noqa: E501 Cmems obs-oc glo bgc-reflectance NRT l4-olci-300m p1m
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-4km_P1M_202207",  # noqa: E501 Cmems obs-oc glo bgc-reflectance NRT l4-olci-4km p1m
    "cmems_obs-oc_glo_bgc-transp_nrt_l4-gapfree-multi-4km_P1D_202207",  # noqa: E501 Cmems obs-oc glo bgc-transp NRT l4-gapfree-multi-4km p1d
    "cmems_obs-oc_glo_bgc-transp_nrt_l4-multi-4km_P1M_202207",  # noqa: E501 Cmems obs-oc glo bgc-transp NRT l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-transp_nrt_l4-olci-4km_P1M_202207",  # noqa: E501 Cmems obs-oc glo bgc-transp NRT l4-olci-4km p1m
]


class oceancolour_glo_bgc_l4_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L4_NRT_009_102"
    dataset = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L4_NRT_009_102"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "BBP",
            "BBP_uncertainty",
            "CDM",
            "CDM_uncertainty",
            "CHL",
            "CHL_uncertainty",
            "DIATO",
            "DIATO_uncertainty",
            "DINO",
            "DINO_uncertainty",
            "GREEN",
            "GREEN_uncertainty",
            "HAPTO",
            "HAPTO_uncertainty",
            "KD490",
            "KD490_uncertainty",
            "MICRO",
            "MICRO_uncertainty",
            "NANO",
            "NANO_uncertainty",
            "PICO",
            "PICO_uncertainty",
            "PP",
            "PP_uncertainty",
            "PROCHLO",
            "PROCHLO_uncertainty",
            "PROKAR",
            "PROKAR_uncertainty",
            "RRS400",
            "RRS400_uncertainty",
            "RRS412",
            "RRS412_uncertainty",
            "RRS443",
            "RRS443_uncertainty",
            "RRS490",
            "RRS490_uncertainty",
            "RRS510",
            "RRS510_uncertainty",
            "RRS555",
            "RRS555_uncertainty",
            "RRS560",
            "RRS560_uncertainty",
            "RRS620",
            "RRS620_uncertainty",
            "RRS665",
            "RRS665_uncertainty",
            "RRS670",
            "RRS670_uncertainty",
            "RRS674",
            "RRS674_uncertainty",
            "RRS681",
            "RRS681_uncertainty",
            "RRS709",
            "RRS709_uncertainty",
            "SPM",
            "SPM_uncertainty",
            "ZSD",
            "ZSD_uncertainty",
            "flags",
            "lat",
            "lon",
            "time",
        ],
        multiple=True,
    )
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        layer,
        area=None,
        variables=None,
        start=None,
        end=None,
    ):
        if layer == "cmems_obs-oc_glo_bgc-optics_nrt_l4-multi-4km_P1M_202207":
            if start is None:
                start = "2023-07-31T20:42:00Z"

            if end is None:
                end = "2023-09-01T02:19:59Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-4km_P1M_202207":
            if start is None:
                start = "2023-07-31T20:15:42Z"

            if end is None:
                end = "2023-09-01T00:43:43Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-4km_P1M_202207":
            if start is None:
                start = "2023-07-31T20:15:42Z"

            if end is None:
                end = "2023-09-01T00:43:43Z"

        if layer == "cmems_obs-oc_glo_bgc-pp_nrt_l4-multi-4km_P1M_202207":
            if start is None:
                start = "2023-07-31T16:30:01Z"

            if end is None:
                end = "2023-09-01T04:02:00Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_nrt_l4-gapfree-multi-4km_P1D_202207":
            if start is None:
                start = "2023-09-16T20:04:11Z"

            if end is None:
                end = "2023-09-25T03:09:10Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-300m_P1M_202211":
            if start is None:
                start = "2023-07-31T20:55:13Z"

            if end is None:
                end = "2023-08-31T23:44:19Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-300m_P1M_202211":
            if start is None:
                start = "2023-07-31T20:55:13Z"

            if end is None:
                end = "2023-08-31T23:44:19Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_nrt_l4-olci-4km_P1M_202207":
            if start is None:
                start = "2023-07-31T20:15:42Z"

            if end is None:
                end = "2023-09-01T00:43:43Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-multi-4km_P1M_202207":
            if start is None:
                start = "2023-07-31T20:42:00Z"

            if end is None:
                end = "2023-09-01T02:19:59Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_nrt_l4-gapfree-multi-4km_P1D_202207":
            if start is None:
                start = "2023-09-16T20:04:11Z"

            if end is None:
                end = "2023-09-25T03:09:10Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_nrt_l4-multi-4km_P1M_202207":
            if start is None:
                start = "2023-07-31T16:30:01Z"

            if end is None:
                end = "2023-09-01T04:02:00Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_nrt_l4-multi-4km_P1M_202207":
            if start is None:
                start = "2023-07-31T16:30:01Z"

            if end is None:
                end = "2023-09-01T04:02:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
