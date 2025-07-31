from dataclasses import dataclass, field
from typing import List, Union, Dict, Any
from enum import Enum, auto
from nonebot.adapters.onebot.v11 import MessageSegment

# 用户ID的来源
class UserSource(Enum):
    AT_MENTION = auto()  # 来源于@
    RAW_ID = auto()      # 来源于QQ号

@dataclass
class ParsedNode:
    uin: str
    source: UserSource
    content: List[Union[str, 'ParsedNode']] = field(default_factory=list)

class ForwardNodeData(Dict[str, Any]):
    name: str
    uin: str
    content: Union[MessageSegment, List[Union[MessageSegment, Dict[str, Any]]]]

class ForwardNode(Dict[str, Any]):
    type: str
    data: ForwardNodeData