Microservices:
* Cart
* testingAPI
* ordersAPI

API GATEWAY:

* reds

FRONTEND APP:
 * reds_vue


TO RUN:
* Download requirements.txt & paste in the root directory
* Create a virtual environment
* install those requirements
* RUN batfiles/check the bat files(commands)

TO EXECUTE
<Virtual Environment>(pipenv shell)
* <reds> python manage.py 8001 runserver
  
* <testingAPI> python manage.py runserver
  
* <testingAPI> python manage.py localhost:50051 grpcrunserver
  
* <ordersAPI> python manage.py localhost:50052 grpcrunserver
  
* <cart> python manage.py localhost:50053 grpcrunserver
  
* <reds_vue> npm run serve
  
