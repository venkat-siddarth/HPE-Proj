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
* <b>reds</b> python manage.py 8001 runserver
  
* <b>testingAPI</b> python manage.py runserver
  
* <b>testingAPI</b> python manage.py localhost:50051 grpcrunserver
  
* <b>ordersAPI</b> python manage.py localhost:50052 grpcrunserver
  
* <b>cart</b> python manage.py localhost:50053 grpcrunserver
  
* <b>reds_vue</b> npm run serve
  
