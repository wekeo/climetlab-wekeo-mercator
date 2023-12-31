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
    "cmems_obs-oc_blk_bgc-optics_nrt_l3-multi-1km_P1D_202207",  # noqa: E501 Cmems obs-oc blk bgc-optics NRT l3-multi-1km p1d
    "cmems_obs-oc_blk_bgc-plankton_nrt_l3-multi-1km_P1D_202211",  # noqa: E501 Cmems obs-oc blk bgc-plankton NRT l3-multi-1km p1d
    "cmems_obs-oc_blk_bgc-plankton_nrt_l3-olci-300m_P1D_202207",  # noqa: E501 Cmems obs-oc blk bgc-plankton NRT l3-olci-300m p1d
    "cmems_obs-oc_blk_bgc-reflectance_nrt_l3-multi-1km_P1D_202207",  # noqa: E501 Cmems obs-oc blk bgc-reflectance NRT l3-multi-1km p1d
    "cmems_obs-oc_blk_bgc-reflectance_nrt_l3-olci-300m_P1D_202207",  # noqa: E501 Cmems obs-oc blk bgc-reflectance NRT l3-olci-300m p1d
    "cmems_obs-oc_blk_bgc-transp_nrt_l3-multi-1km_P1D_202207",  # noqa: E501 Cmems obs-oc blk bgc-transp NRT l3-multi-1km p1d
    "cmems_obs-oc_blk_bgc-transp_nrt_l3-olci-300m_P1D_202207",  # noqa: E501 Cmems obs-oc blk bgc-transp NRT l3-olci-300m p1d
]


class oceancolour_blk_bgc_l3_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_BLK_BGC_L3_NRT_009_151"
    dataset = "EO:MO:DAT:OCEANCOLOUR_BLK_BGC_L3_NRT_009_151"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "ADG443",
            "APH443",
            "BBP443",
            "CHL",
            "KD490",
            "MICRO",
            "NANO",
            "PICO",
            "QI_ADG443",
            "QI_APH443",
            "QI_BBP443",
            "QI_CHL",
            "QI_KD490",
            "QI_RRS412",
            "QI_RRS412_5",
            "QI_RRS442_5",
            "QI_RRS443",
            "QI_RRS490",
            "QI_RRS510",
            "QI_RRS555",
            "QI_RRS560",
            "QI_RRS670",
            "QI_RRS673_75",
            "RRS400",
            "RRS412",
            "RRS412_5",
            "RRS442_5",
            "RRS443",
            "RRS490",
            "RRS510",
            "RRS555",
            "RRS560",
            "RRS620",
            "RRS665",
            "RRS670",
            "RRS673_75",
            "RRS681_25",
            "RRS708_75",
            "RRS778_75",
            "RRS865",
            "SENSORMASK",
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
        if layer == "cmems_obs-oc_blk_bgc-transp_nrt_l3-multi-1km_P1D_202207":
            if start is None:
                start = "2023-09-17T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-optics_nrt_l3-multi-1km_P1D_202207":
            if start is None:
                start = "2023-09-17T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-plankton_nrt_l3-multi-1km_P1D_202211":
            if start is None:
                start = "2023-09-17T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-transp_nrt_l3-olci-300m_P1D_202207":
            if start is None:
                start = "2023-09-17T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-reflectance_nrt_l3-multi-1km_P1D_202207":
            if start is None:
                start = "2023-09-17T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-plankton_nrt_l3-olci-300m_P1D_202207":
            if start is None:
                start = "2023-09-17T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        if layer == "cmems_obs-oc_blk_bgc-reflectance_nrt_l3-olci-300m_P1D_202207":
            if start is None:
                start = "2023-09-17T00:00:00Z"

            if end is None:
                end = "2023-09-24T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
