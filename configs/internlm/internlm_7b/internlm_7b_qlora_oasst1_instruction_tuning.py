from mmengine.config import read_base

from mmchat.engine import LogSampleHook, SampleGenerateHook
from mmchat.utils import PROMPT_TEMPLATE

with read_base():
    from ..._base_.datasets.oasst1_instruction_tuning import *  # noqa: F401,F403,E501
    from ..._base_.default_runtime import *  # noqa: F401,F403
    from ..._base_.models.internlm_7b_qlora import *  # noqa: F401,F403
    from ..._base_.schedules.cosine_e3 import *  # noqa: F401,F403

train_dataloader.dataset.tokenizer = tokenizer  # noqa: F405

custom_hooks = [
    dict(type=LogSampleHook, tokenizer=tokenizer),  # noqa: F405
    dict(
        type=SampleGenerateHook,
        tokenizer=tokenizer,  # noqa: F405
        every_n_iters=500,
        stop_word='###',
        sample_inputs=[
            '请给我介绍五个上海的景点', 'Please tell me five scenic spots in Shanghai'
        ],
        instruction=PROMPT_TEMPLATE.openassistant.INSTRUCTION_START)
]