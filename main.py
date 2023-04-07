from datetime import datetime
from Timezone_class import TimeZone


tz1 = TimeZone('ABC', -2, -15)
dt = datetime.utcnow()

print(tz1.name)