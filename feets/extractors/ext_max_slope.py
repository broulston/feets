#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The MIT License (MIT)

# Copyright (c) 2017 Juan Cabral

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# =============================================================================
# DOC
# =============================================================================

""""""


# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np

from .core import Extractor


# =============================================================================
# EXTRACTOR CLASS
# =============================================================================

class MaxSlope(Extractor):
    """
    **MaxSlope**

    Maximum absolute magnitude slope between two consecutive observations.

    Examining successive (time-sorted) magnitudes, the maximal first difference
    (value of delta magnitude over delta time)

    .. code-block:: pycon

        >>> fs = feets.FeatureSpace(only=['MaxSlope'])
        >>> features, values = fs.extract(**lc_normal)
        >>> dict(zip(features, values))
        {'MaxSlope': 5.4943105823904741}

    References
    ----------

    .. [richards2011machine] Richards, J. W., Starr, D. L., Butler, N. R.,
       Bloom, J. S., Brewer, J. M., Crellin-Quick, A., ... &
       Rischard, M. (2011). On machine-learned classification of variable stars
       with sparse and noisy time-series data.
       The Astrophysical Journal, 733(1), 10. Doi:10.1088/0004-637X/733/1/10.


    """

    data = ['magnitude', 'time']
    features = ["MaxSlope"]
    params = {"timesort": True}

    def fit(self, magnitude, time, timesort):
        if timesort:
            sort = np.argsort(time)
            time, magnitude = time[sort], magnitude[sort]

        slope = np.abs(magnitude[1:] - magnitude[:-1]) / (time[1:] - time[:-1])
        return {"MaxSlope": np.max(slope)}
