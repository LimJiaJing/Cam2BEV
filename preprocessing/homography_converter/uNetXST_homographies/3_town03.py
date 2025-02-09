# ==============================================================================
# MIT License
#
# Copyright 2020 Institute for Automotive Engineering of RWTH Aachen University.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

import numpy as np

# for dataset 3_town03
H = [
  np.array([[-1.4102530788152077e-14, 10.102317552963292, -5.315811711761264e-07], [-5.539293896370624e-07, -3.550620662776533e-23, 1.616581756984388], [34.995433142005, 2.2431651098749346e-15, -0.9000018414500918]]),                                       # front
  np.array([[2.514773446106109e-14, -10.102317552963292, 5.315811726454487e-07], [5.539293833561938e-07, 3.550620622516922e-23, 1.6165817671146285], [-34.995433142004984, -2.2431651098749334e-15, -1.539998158549916]]), # rear
  np.array([[20.204635105926595, 1.4102530166876163e-14, -1.0631623462364152e-06], [-3.391839269863376e-23, 2.7696469481853097e-07, 1.616581751919173], [2.142852259106598e-15, -17.49771657100263, -0.5799990792749558]]),    # left
  np.array([[-20.20463510592659, -6.439800384095345e-14, 1.0631623452122295e-06], [-3.3918392111051626e-23, -2.769646948185295e-07, 1.6165817519192023], [2.1428522591065863e-15, 17.497716571002538, -0.5800009207250398]])   # right
]

"""
OpenCV homography for front:
[[-6.344959136241835e-18, 1.2689956999067142, -369.4634763718277], [0.04949359105658629, 0.775161564717514, -257.9547034339638], [-0.0, 0.0025667601480712393, -0.7751615647175143]]
OpenCV homography for rear:
[[6.344959136241835e-18, 1.1827354412081057, -370.959328244848], [-0.04949359105658629, 0.7751615647175225, -210.24288165541725], [-0.0, 0.0025667601480712674, -0.7751615647175228]]
OpenCV homography for left:
[[0.04949359105658626, 1.2371783913703474, -397.4837850831194], [3.0306083932878225e-18, 0.7546570769940779, -241.6796622522115], [-0.0, 0.0025667601480712605, -0.7751615647175207]]
OpenCV homography for right:
[[-0.049493591056586274, 1.2371783913703471, -349.7719633045703], [3.0306083932878336e-18, 0.7956660524409636, -226.517922837171], [3.7322671730688436e-35, 0.0025667601480712605, -0.7751615647175207]]



"""