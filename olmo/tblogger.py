import os.path as osp
from torch.utils.tensorboard import SummaryWriter


# create a new class inheriting from tensorboardX.SummaryWriter
class NewSummaryWriter(SummaryWriter):


    def __init__(self, log_dir=None, comment="", **kwargs):
        super().__init__(log_dir, comment, **kwargs)


    # create a new function that will take dictionary as input
    # and uses built-in add_scalar() function
    # that function combines all plots into one subgroup by a tag
    def add_scalar_dict(self, dictionary, global_step, tag=None):
        for name, val in dictionary.items():
            if tag is not None:
                name = osp.join(tag, name)
            self.add_scalar(name, val, global_step)


writer = None


def init(log_dir=None):
  global writer
  writer = NewSummaryWriter(log_dir=log_dir)


def log(dictionary, global_step, tag=None):
  global writer
  writer.add_scalar_dict(dictionary, global_step, tag)


def finish():
  writer.close()

