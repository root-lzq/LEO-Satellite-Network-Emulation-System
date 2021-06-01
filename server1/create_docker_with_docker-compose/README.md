* The results of tests show that this method docker-compose is not suitable for creating a large number of containers/services.
* It is recommended that the number of containers/services should be less than 200, otherwise it will take a long time to create containers/services.
* In the process of creating containers/services, you may encounter a WARNING "**Connection pool is full, discarding Connection: localhost**"
* If you can solve this WARNING, you may be able to use this method docker-compose to create far more than 200 containers/services in an acceptable time. Good luck!
