import subprocess
from pathlib import Path

from .harness import Harness


class TestBasic(Harness):
    '''
    Verify that we can run the default matrix suite on the basic
    bundle, in reasonable time.

    '''
    def setUp(self):
        super(TestBasic, self).setUp()
        self.artifacts = ['matrix.log', 'chaos_plan*.yaml']

    def test_basics(self):
        subprocess.run(self.cmd, timeout=1000)
        self.check_artifacts(2)  # 1 chaos plan, and a log
