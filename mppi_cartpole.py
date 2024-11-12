import numpy as np
import mujoco
from copy import deepcopy
import mujoco_viewer

model = mujoco.MjModel.from_xml_path('cartpole.xml')
data = mujoco.MjData(model)
viewer = mujoco_viewer.MujocoViewer(model, data)

# TODO Understand data.ctrl, model.geom, data.qpos, data.qvel


while True:
    #TODO Add control logic

    if viewer.is_alive:
        mujoco.mj_step(model, data)
        viewer.render()
    else:
        break


# close
viewer.close()
