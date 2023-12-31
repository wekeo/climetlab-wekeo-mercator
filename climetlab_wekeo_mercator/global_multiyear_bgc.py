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
    "cmems_mod_glo_bgc_my_0.25_P1D-m_202112",  # noqa: E501 Daily mean fields for product global reanalysis bio 001 029
    "cmems_mod_glo_bgc_my_0.25_P1M-m_202112",  # noqa: E501 Monthly mean fields for product global reanalysis bio 001 029
]


class global_multiyear_bgc(Main):
    name = "EO:MO:DAT:GLOBAL_MULTIYEAR_BGC_001_029"
    dataset = "EO:MO:DAT:GLOBAL_MULTIYEAR_BGC_001_029"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize(
        "variables",
        [
            "chl",
            "depth",
            "fe",
            "latitude",
            "longitude",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "po4",
            "si",
            "spco2",
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
        if layer == "cmems_mod_glo_bgc_my_0.25_P1M-m_202112":
            if start is None:
                start = "2021-12-01T00:00:00Z"

            if end is None:
                end = "2021-12-28T00:00:00Z"

        if layer == "cmems_mod_glo_bgc_my_0.25_P1D-m_202112":
            if start is None:
                start = "0001-01-01T00:00:00Z"

            if end is None:
                end = "9991-12-28T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            variables=variables,
            start=start,
            end=end,
        )
