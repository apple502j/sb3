import unittest
import sys, os.path
sys.path.append(os.path.realpath(".."))
import sb3

class SB3Test(unittest.TestCase):
    def setUp(self):
        self.project, self.assets = sb3.open_sb3("testcase.sb3")

    def test_meta(self):
        meta = self.project.meta
        self.assertEqual(repr(meta), "<Meta>", "meta: repr()")
        self.assertEqual(meta.semantic_ver, "3.0.0", "meta: semantic_ver")
        self.assertEqual(meta.vm_ver, "0.2.0-prerelease.20190822194548", "meta: vm_ver")

    def test_assets(self):
        self.assertEqual(len(self.assets), 7, "assets: asset count")

    def test_extensions(self):
        self.assertEqual(self.project.extensions, ["makeymakey", "text2speech", "videoSensing"], "extensions: extensions")

    def test_monitors(self):
        monitors = self.project.monitors
        self.assertEqual(len(monitors), 8, "monitors: monitor count")
        monitor_0 = monitors[0]
        self.assertEqual(monitor_0.id, "5E:HGSM(6DJ3V6!clQ@Z", "monitors: monitor id")
        self.assertEqual(monitor_0.x, 5, "monitors: monitor X pos")
        self.assertEqual(monitor_0.opcode, "data_variable", "monitors: opcode")
        self.assertIs(monitor_0.visible, False, "monitors: visibility")
        self.assertEqual(monitor_0.params.VARIABLE, "ねこの変数", "monitors: params")

        self.assertEqual(monitors[5].params.CURRENTMENU, "MONTH", "monitors: current () block handling")

    def test_targets(self):
        targets = self.project.targets
        target_0 = targets[0]
        self.assertIsInstance(target_0, sb3.Stage, "targets: stage isinstance()")
        self.assertEqual(target_0.name, "Stage", "targets: stage name")
        self.assertEqual(target_0.layer, 0, "targets: stage layer")
        self.assertEqual(target_0.video_state, "on-flipped", "targets: video state")
        variables = target_0.variables
        self.assertEqual(len(variables), 2, "targets: variable count")
        self.assertEqual(variables[1].id, "6-UJ,OT7]alDggT;OtO`", "targets: variable id")
        broadcasts = target_0.broadcasts
        self.assertEqual(len(broadcasts), 1, "targets: broadcast count")
        self.assertEqual(broadcasts[0].name, "loud", "targets: broadcast name")
        sounds = target_0.sounds
        self.assertEqual(len(sounds), 1, "targets: sound count")
        self.assertEqual(sounds[0].asset_id, "83a9787d4cb6f3b7632b4ddfebf74367", "targets: sound asset ID")

        target_1 = targets[1]
        comments = target_1.comments
        self.assertEqual(len(comments), 3, "targets: comment count")
        self.assertEqual(comments[0].id, "t.xEhIa3wtU*w5AOK3Eb", "targets: comment id")
        self.assertIs(comments[0].minimized, False, "targets: comment minimized")

        block = target_1.block_info
        self.assertEqual(len(block.scripts()), 4, "target: script counts")
        self.assertIs(block.scripts()[2][0].isolated, True, "target: block isolated")
        self.assertEqual(block.scripts()[0][0].opcode, "event_whenflagclicked", "target: block opcode")
        self.assertEqual(block.blocks()[0].next, block.blocks()[11], "target: block.next")
        self.assertEqual(block.blocks()[7].inputs[1].block.id, "jq}7@gdupgvqfHC+t3[e", "target: block input")
        self.assertEqual(block.blocks()[8].fields[0].value, "volume", "target: block field")

if __name__ == '__main__':
    unittest.main()
