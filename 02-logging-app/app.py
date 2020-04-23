from models import MicroserviceLog

# Create a service log
log1 = MicroserviceLog(
    title='Start Product Service fail',
    log_type='application',
    log_details='Error connection to database'
)

log2 = MicroserviceLog(
    title='Start Order Service fail',
    log_type='application',
    log_details='Error parsing datetime'
)



if __name__ == '__main__':
    log1.save()
    log2.save()

