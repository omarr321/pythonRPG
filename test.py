from bin.gameClasses.items import Effect
from bin.gameClasses.items import EffectStatus

temp = Effect(EffectStatus.HEAL, [1,5])
print(temp.toSave())