# PRP
# 安全参数
我暂时设定的参数范围：   
      s:2^4090   
      p:2^4096   
      alpha:2^500    
      r:2^100    
      L:1000   
## Security_Parameter.dat
每三行为一组，依次存放s,alpha,p，共10组；
这样的目的是因为我想把初始化参数的过程分离出来，prime.dat先作废
