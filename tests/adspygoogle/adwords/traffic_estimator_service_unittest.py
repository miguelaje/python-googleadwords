#!/usr/bin/python
#
# Copyright 2010 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests to cover TrafficEstimator."""

__author__ = 'api.sgrinberg@gmail.com (Stan Grinberg)'

import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..'))
import unittest

from tests.adspygoogle.adwords import HTTP_PROXY
from tests.adspygoogle.adwords import SERVER_V201109
from tests.adspygoogle.adwords import TEST_VERSION_V201109
from tests.adspygoogle.adwords import VERSION_V201109
from tests.adspygoogle.adwords import client


class TrafficEstimatorServiceTestV201109(unittest.TestCase):

  """Unittest suite for TrafficEstimatorService using v201109."""

  SERVER = SERVER_V201109
  VERSION = VERSION_V201109
  client.debug = False
  service = None

  def setUp(self):
    """Prepare unittest."""
    print self.id()
    if not self.__class__.service:
      self.__class__.service = client.GetTrafficEstimatorService(
          self.__class__.SERVER, self.__class__.VERSION, HTTP_PROXY)

  def testKeywordTrafficEstimates(self):
    """Test whether we can estimate keyword traffic."""
    selector = {
        'campaignEstimateRequests': [{
            'adGroupEstimateRequests': [{
                'keywordEstimateRequests': [
                    {
                        'keyword': {
                            'xsi_type': 'Keyword',
                            'matchType': 'BROAD',
                            'text': 'mars cruise'
                        },
                        'maxCpc': {
                            'xsi_type': 'Money',
                            'microAmount': '1000000'
                        }
                    },
                    {
                        'keyword': {
                            'xsi_type': 'Keyword',
                            'matchType': 'PHRASE',
                            'text': 'cheap cruise'
                        },
                        'maxCpc': {
                            'xsi_type': 'Money',
                            'microAmount': '1000000'
                        }
                    },
                    {
                        'keyword': {
                            'xsi_type': 'Keyword',
                            'matchType': 'EXACT',
                            'text': 'cruise'
                        },
                        'maxCpc': {
                            'xsi_type': 'Money',
                            'microAmount': '1000000'
                        }
                    }
                ],
                'maxCpc': {
                    'xsi_type': 'Money',
                    'microAmount': '1000000'
                }
            }],
            'criteria': [
                {
                    'xsi_type': 'Location',
                    'id': '2044'
                },
                {
                    'xsi_type': 'Language',
                    'id': '1000'
                }
            ]
        }]
    }
    self.assert_(isinstance(self.__class__.service.Get(selector), tuple))


def makeTestSuiteV201109():
  """Set up test suite using v201109.

  Returns:
    TestSuite test suite using v201109.
  """
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(TrafficEstimatorServiceTestV201109))
  return suite


if __name__ == '__main__':
  suites = []
  if TEST_VERSION_V201109:
    suites.append(makeTestSuiteV201109())
  if suites:
    alltests = unittest.TestSuite(suites)
    unittest.main(defaultTest='alltests')
