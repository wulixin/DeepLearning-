"""数据采集模块"""

from .collector import (
    BaseDataCollector,
    EastMoneyCollector,
    SinaCollector,
    DataCollectorFactory,
    get_latest_volume,
    get_history_volumes
)

__all__ = [
    'BaseDataCollector',
    'EastMoneyCollector',
    'SinaCollector',
    'DataCollectorFactory',
    'get_latest_volume',
    'get_history_volumes'
]
