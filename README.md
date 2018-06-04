# Workbook: Algorithms and Data Sctructures #

## alpha ##
Ref:  `nymdock001@/usr/local/share/docker/hrreqs`


### beta ###
Lipsum ipsum
```bash
virtualenv dev
```

### Django Setup ###
`django-admin startproject project`

`python manage.py startapp hrreqs`

[Reset schema.](https://stackoverflow.com/a/27583836)

#### Initiaize ####
And this creates some initial useful records in the database (Django):
```python
from hrreqs.models import *
from django.utils import timezone
timezone.now()

config = [
       {
	'data': ['artist', 'corporate', 'design', 'hr', 'operations', 'pipeline', 'production', 'systems'],
		'class': Department,
		},
		{
			'data': ['la', 'ny'],
				'class': Location,
				},
				{
					'data': ['new position', 'replacement'],
						'class': Reason,
						},
						{
							'data': ['ceo / cfo / coo', 'hiring manager', 'hr', 'managing director'],
								'class': Sigtype,
								},
								{
									'data': ['approved', 'cancelled', 'denied', 'hold', 'new'],
										'class': Status,
										},
										{
											'data': ['blacklist', 'psyop'],
												'class': Unit,
												},
]

for c in config:
    for name in c['data']:
    	thing = c['class'](name=name)
	      thing.save()
```

| var    | value         |
| -----  | ------------- |
| user   | admin         |
| pass   | 1qazXSW@      |
| email  | wfan@psyop.tv |

