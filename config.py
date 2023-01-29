from dataclasses import dataclass

@dataclass()
class Config:
    '''Конфиг бота, легко настраиваемый'''
    token: str = '' # токен от бота
    cid: int = -1 # ID канала
    mid: int = 204 # ID сообщения
    final_time: int = 1675231200 # дата окончания отсчёта (пр. 1 февраля 2023, 9:00)