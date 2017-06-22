# check-beanstalkd

A [Nagios]/[Icinga] plugin for checking connectivity to an [beanstalk] instance. 

This plugin connects to the specified beanstalkd instance. Upon successful connection, the overall or tube specific statistics are evaluated.

## Configuration

Configuration can be done via the following command line arguments:

```
usage: check-beanstalkd.py
	[-h hostname/address]   // default localhost
	[-p port]               // default 11300
	[-w warning-threshold]  // default 8
	[-c critical-threshold] // default 10
	[-t tubename]           // default None
	[-s stats entry]        // default current-jobs-ready
```

## Example


```
$ ./check_beanstalkd.py -h localhost -p 11300 -w 5 -c 10 -s current-jobs-buried
WARNING beanstalkd | current-jobs-buried=6
```


## Nagios Configuration
### command definition
```
define command{
        command_name    check-beanstalkd
        command_line    $USER1$/check_beanstalkd.py
        }
        
```

### service definition
```
define service{
        use                             local-service
        host_name                       localhost
        service_description             beanstalkd instance
        check_command                   check-beanstalkd
        notifications_enabled           0
        }
        
```

 [nagios]: http://nagios.org
 [icinga]: http://icinga.org
 [beanstalk]: https://github.com/kr/beanstalkd
