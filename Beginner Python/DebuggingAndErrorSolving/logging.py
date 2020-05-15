import logging
#please run this program on IDLE python if any problem arrives
logging.basicConfig(level=logging.DEBUG , format=' %(asctime)s - %(levelname)s - %(message)s')
#to write all logs in file you need to change in basicConfig
#logging.basicConfig(filename='myprogramLog.txt' , level=logging.DEBUG , format=' %(asctime)s - %(levelname)s - %(message)s')









#to disable logging messages after your work is done
#then
#logging.disable(logging.CRITICAL)

logging.debug('Start of program (%s)')

#there are five levels of logginng debug(very low level) ->info->warning -> error -> critical (high level)
logging.info('this is logging.info()')
logging.warning('this is logging.warning()')
logging.error('this is logging.error()')
logging.critical('this is logging.critical()')

#start of factorial program
def factorial(n):
	logging.debug('Start of program (%s)' % (n))
	total=1
	for i in range(n+1):
		total=total*i
		logging.debug('i is (%s) and total is (%s)' %(i , total))
	logging.debug('return value is (%s)'%(total))
	return total



print(factorial(7))  #it gets 0 answer

logging.debug('End of program')

