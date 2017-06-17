#from ctaBase import *
#from ctaTemplate import CtaTemplate
import os,sys
import json
print "hello world!"

########################################################################
#//class PirateStrategy(CtaTemplate):
class PirateStrategy(object):
    """海盗交易策略"""
    settingFileName = 'pirate_setting.json'
    path = os.path.abspath(os.path.dirname(__file__))
    settingFileName = os.path.join(path, settingFileName)      

    maket_situation = 0; #0 区间震荡，1 趋势多，2 趋势空 
    strategy_type = 1; #0 
    y_open_price = 1; #yestday opening price
    y_close_price = 2;
    y_highest_price = 1;
    y_lowest_price = 1;
    M20_high = 21;
    M20_low = 123;
    
    
    #----------------------------------------------------------------------
    def __init__(self):
    #def __init__(self, ctaEngine, setting):
        #"""Constructor"""
        #super(EmaDemoStrategy, self).__init__(ctaEngine, setting)
        
        # 注意策略类中的可变对象属性（通常是list和dict等），在策略初始化时需要重新创建，
        # 否则会出现多个策略实例之间数据共享的情况，有可能导致潜在的策略逻辑错误风险，
        # 策略类中的这些可变对象属性可以选择不写，全都放在__init__下面，写主要是为了阅读
        # 策略时方便（更多是个编程习惯的选择）
        self.fastMa = []
        self.slowMa = []    
    #----------------------------------------------------------------------
    def loadStrategySetting(self):
        with open(self.settingFileName, 'r') as f:
            
                data = json.load(f)
                return data
        
    #----------------------------------------------------------------------
    def onInit(self):
        
        pass
    #----------------------------------------------------------------------
    def onStart(self):
        pass

    #----------------------------------------------------------------------
    def onStop(self):
        pass 
        
    #----------------------------------------------------------------------
    def onTick(self, tick):
        pass
    
if __name__ == "__main__":
    stategy = PirateStrategy()
    data = stategy.loadStrategySetting()
    print data['selected']
    