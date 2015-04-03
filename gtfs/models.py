import uuid
from django.db import models

class DataSet(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )
    name = models.CharField(
        max_length = 128,
        blank = True,
        default = u'',
        verbose_name = 'Name',
    )
    note = models.TextField(
        blank = True,
        default = u'',
        verbose_name = u'Notes'
    )
    class Meta:
        verbose_name = u'Data Set'
        verbose_name_plural = u'Data Sets'
        ordering = ['name',]
    def __unicode__(self):
        return self.name

class Timezone(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length = 128,
        blank = False,
        unique = True,
        help_text = u'Zone name used in value of TZ environment variable.'
    )
    utc_offset = models.CharField(
        max_length = 10,
        blank = True,
        default = u'',
    )
    class Meta:
        verbose_name = u'Timezone'
        verbose_name_plural = u'Timezones'
        ordering = ['name',]
    def __unicode__(self):
        return ''.join([self.name,' (UTC',self.utc_offset,')'])

class Language(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    iso_639_1 = models.CharField(
        max_length = 2,
        blank = True,
        default = '',
        unique = True,
        help_text = u'ISO 639-1 alpha-2 language code.'
    )
    name = models.CharField(
        max_length = 128,
        blank = False,
        unique = True,
        help_text = u'English name of language.'
    )
    class Meta:
        verbose_name = u'Language'
        verbose_name_plural = u'Languages'
        ordering = ['iso_639_1',]
    def __unicode__(self):
        return u': '.join([self.iso_639_1, self.name,])

class Agency(models.Model): # For agency.txt (REQUIRED)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    agency_id = models.CharField(
        max_length = 64,
        blank = True,
        null = True,
        verbose_name = u'Agency ID',
        help_text = u'The agency_id field is an ID that uniquely identifies a transit agency. A transit feed may represent data from more than one agency. The agency_id is dataset unique. This field is optional for transit feeds that only contain data for a single agency.',
    )
    agency_name = models.CharField(
        max_length = 255,
        blank = False,
        null = False,
        verbose_name = u'Agency Name',
        help_text = u'The agency_name field contains the full name of the transit agency. Google Maps will display this name.'
    )
    agency_url = models.URLField(
        max_length = 255,
        blank = False,
        null = False,
        help_text = u'The agency_url field contains the URL of the transit agency. The value must be a fully qualified URL that includes http:// or https://, and any special characters in the URL must be correctly escaped. See http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values.'
    )
    agency_timezone = models.ForeignKey(
        Timezone,
        null = False,
        help_text = u'The agency_timezone field contains the timezone where the transit agency is located. Timezone names never contain the space character but may contain an underscore. If multiple agencies are specified in the feed, each must have the same agency_timezone.'
    )
    agency_lang = models.ForeignKey(
        Language,
        null = True,
        help_text = u'A two-letter ISO 639-1 code for the primary language used by this transit agency. The language code is case-insensitive (both en and EN are accepted). This setting defines capitalization rules and other language-specific settings for all text contained in this transit agency\'s feed.',
    )
    agency_phone = models.CharField(
        max_length = 20,
        blank = True,
        default = u'',
        help_text = u'The agency_phone field contains a single voice telephone number for the specified agency. This field is a string value that presents the telephone number as typical for the agency\'s service area. It can and should contain punctuation marks to group the digits of the number. Dialable text (for example, TriMet\'s "503-238-RIDE") is permitted, but the field must not contain any other descriptive text.',
    )
    agency_fare_url = models.URLField(
        max_length=255,
        blank = True,
        default = u'',
        help_text = u'The agency_fare_url specifies the URL of a web page that allows a rider to purchase tickets or other fare instruments for that agency online. The value must be a fully qualified URL that includes http:// or https://, and any special characters in the URL must be correctly escaped. See http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values.',
    )
    data_set = models.ForeignKey(
        DataSet,
        null = True,
    )
    class Meta:
        verbose_name = u'Agency'
        verbose_name_plural = u'Agencies'
        ordering = ['agency_id',]
    def __unicode__(self):
        return self.agency_name


class Route(models.Model): # For routes.txt (REQUIRED)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    route_id = models.CharField(
        max_length = 100
    )
    agency = models.ForeignKey(Agency)
    route_short_name = models.CharField(
        max_length = 100,
    )
    route_long_name = models.CharField(
        max_length = 200,
    )
    route_desc = models.CharField(
        max_length = 255,
        blank = True,
        default = u'',
    )
    ROUTE_TYPE_CHOICES = (
        ('0', 'Tram, Streetcar, Light rail. Any light rail or street level system within a metropolitan area.'),
        ('1', 'Subway, Metro. Any underground rail system within a metropolitan area.'),
        ('2', 'Rail. Used for intercity or long-distance travel.'),
        ('3', 'Bus. Used for short- and long-distance bus routes.'),
        ('4', 'Ferry. Used for short- and long-distance boat service.'),
        ('5', 'Cable car. Used for street-level cable cars where the cable runs beneath the car.'),
        ('6', 'Gondola, Suspended cable car. Typically used for aerial cable cars where the car is suspended from the cable.'),
        ('7', 'Funicular. Any rail system designed for steep inclines.'),
    )
    route_type = models.CharField(
        max_length = 1,
        choices = ROUTE_TYPE_CHOICES,
        default = u'0'
    )
    route_url = models.URLField(
        blank = True,
        default = u'',
    )
    route_color = models.CharField(
        max_length = 6,
        blank = True,
        default = u'',
    )
    route_text_color = models.CharField(
        max_length = 6,
        blank = True,
        default = u'',
    )
    class Meta:
        verbose_name = u'Route'
        verbose_name_plural = u'Routes'
        ordering = ['agency__agency_name','route_short_name',]
    def __unicode__(self):
        return " - ".join([self.route_short_name, self.route_long_name])

class Stop(models.Model): # For stops.txt (REQUIRED)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stop_id = models.CharField(
        max_length = 128,
        help_text = u'The stop_id field contains an ID that uniquely identifies a stop or station. Multiple routes may use the same stop. The stop_id is dataset unique.'
    )
    code = models.CharField(
        max_length = 128,
        blank = True,
        default = u'',
        help_text = u'The stop_code field contains short text or a number that uniquely identifies the stop for passengers. Stop codes are often used in phone-based transit information systems or printed on stop signage to make it easier for riders to get a stop schedule or real-time arrival information for a particular stop. The stop_code field should only be used for stop codes that are displayed to passengers. For internal codes, use stop_id. This field should be left blank for stops without a code.',
    )
    name = models.CharField(
        max_length = 200,
        help_text = u'The stop_name field contains the name of a stop or station. Please use a name that people will understand in the local and tourist vernacular.',
    )
    desc = models.CharField(
        max_length = 255,
        blank = True,
        default = u'',
        help_text = u'The stop_desc field contains a description of a stop. Please provide useful, quality information. Do not simply duplicate the name of the stop.',
    )
    lat = models.DecimalField(
        max_digits = 9,
        decimal_places = 6,
        help_text = u'The stop_lat field contains the latitude of a stop or station. The field value must be a valid WGS 84 latitude.',
    )
    lon = models.DecimalField(
        max_digits = 9,
        decimal_places = 6,
        help_text = u'The stop_lon field contains the longitude of a stop or station. The field value must be a valid WGS 84 longitude value from -180 to 180.',
    )
    zone_id = models.CharField(
        max_length = 100,
        blank = True,
        default = u'',
        help_text = u'The zone_id field defines the fare zone for a stop ID. Zone IDs are required if you want to provide fare information using fare_rules.txt. If this stop ID represents a station, the zone ID is ignored.',
    )
    url = models.URLField(
        blank = True,
        default = u'',
        help_text = u'The stop_url field contains the URL of a web page about a particular stop. This should be different from the agency_url and the route_url fields.'
    )
    LOCATION_TYPE_CHOICES = (
        ('0', u'Stop'),
        ('1', u'Station'),
    )
    location_type = models.CharField(
        max_length = 1,
        default = '0',
        choices = LOCATION_TYPE_CHOICES,
        help_text = u'The location_type field identifies whether this stop ID represents a stop or station. Stations may have different properties from stops when they are represented on a map or used in trip planning.'
    )
    # TODO Limit parent_station options to only stop objects that have location_type = 1
    parent_station = models.ForeignKey(
        'self',
        null = True,
        help_text = u'For stops that are physically located inside stations, the parent_station field identifies the station associated with the stop. To use this field, stops.txt must also contain a row where this stop ID is assigned as a station.',
    )
    timezone = models.ForeignKey(
        Timezone,
        null = True,
        help_text = u'The agency_timezone field contains the timezone where the transit agency is located. Timezone names never contain the space character but may contain an underscore. If multiple agencies are specified in the feed, each must have the same agency_timezone.'
    )
    WHEELCHAIR_BOARDING_CHOICES = (
        ('0', u'No Accessibility Info Available'),
        ('1', u'Some vehicles at this stop can be boarded by a rider in a wheelchair'),
        ('2', u'Wheelchair boarding is not possible.'),
    )
    wheelchair_boarding = models.CharField(
        max_length = 1,
        choices = WHEELCHAIR_BOARDING_CHOICES,
        default = '0',
        help_text = u'The wheelchair_boarding field identifies whether wheelchair boardings are possible from the specified stop or station.',
    )
    class Meta:
        verbose_name = u'Stop'
        verbose_name_plural = u'Stops'
        ordering = ['name',]
    def __unicode__(self):
        return self.name


# class Calendar(models.Model): # For calendar.txt (REQUIRED)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     class Meta:
#         verbose_name = u'Calendar'
#         verbose_name_plural = u'Calendars'
#         ordering = ['',]
#
#
# class CalendarDate(models.Model): # For calendar_dates.txt (OPTIONAL)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     class Meta:
#         verbose_name = u'Calendar Date'
#         verbose_name_plural = u'Calendar Dates'
#         ordering = ['',]

# class Shape(models.Model): # shapes.txt (OPTIONAL)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     class Meta:
#         verbose_name = u'Shape'
#         verbose_name_plural = u'Shapes'
#         ordering = ['',]


class Trip(models.Model): # For trips.txt (REQUIRED)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    route = models.ForeignKey(Route)
    # TODO Make so either service_calendar OR service_calendardate is set.
    # service_calendar = models.ForeignKey(
    #     Calendar,
    #     null = True,
    #     verbose_name = u'Service by Calendar',
    # )
    # service_calendardate = models.ForeignKey(
    #     CalendarDate,
    #     null = True,
    #     verbose_name = u'Service by Calendar Date',
    # )
    trip_id = models.CharField(
        max_length = 128,
        verbose_name = u'Trip ID',
        help_text = u'The trip_id field contains an ID that identifies a trip. The trip_id is dataset unique.',
    )
    headsign = models.CharField(
        max_length = 128,
        blank = True,
        default = u'',
        verbose_name = u'Headsign',
        help_text = u'The trip_headsign field contains the text that appears on a sign that identifies the trip\'s destination to passengers. Use this field to distinguish between different patterns of service in the same route. If the headsign changes during a trip, you can override the trip_headsign by specifying values for the the stop_headsign field in stop_times.txt.',
    )
    short_name = models.CharField(
        max_length = 128,
        blank = True,
        default = u'',
        verbose_name = u'Short Name',
        help_text = u'The trip_short_name field contains the text that appears in schedules and sign boards to identify the trip to passengers, for example, to identify train numbers for commuter rail trips. If riders do not commonly rely on trip names, please leave this field blank. A trip_short_name value, if provided, should uniquely identify a trip within a service day; it should not be used for destination names or limited/express designations.',
    )
    DIRECTION_CHOICES = (
        ('0','Primary/Outbound Direction'),
        ('1','Secondary/Inbound Direction'),
    )
    direction = models.CharField(
        max_length = 1,
        choices = DIRECTION_CHOICES,
        default = u'0',
        verbose_name = 'Direction',
    )
    block_id = models.CharField(
        max_length = 128,
        blank = True,
        default = u'',
        verbose_name = u'Block ID',
        help_text = u'The block_id field identifies the block to which the trip belongs. A block consists of two or more sequential trips made using the same vehicle, where a passenger can transfer from one trip to the next just by staying in the vehicle. The block_id must be referenced by two or more trips in trips.txt.',
    )
    # shape = models.ForeignKey(
    #     Shape,
    #     null = True,
    # )
    WHEELCHAIR_CHOICES = (
        ('0', 'No Accessibility Info'),
        ('1', 'Vehicle Can Accommodate at Least One Wheelchair'),
        ('2', 'No Wheelchairs Can be Accommodated'),
    )
    wheelchair_accessible = models.CharField(
        max_length = 1,
        choices = WHEELCHAIR_CHOICES,
        default = u'0',
        verbose_name = u'Wheelchair Accessibility'
    )
    BIKE_CHOICES = (
        ('0', 'No Bike Info Available'),
        ('1', 'Bicycles Are Allowed'),
        ('2', 'Bicycles Are Not Allowed'),
    )
    bike_access = models.CharField(
        max_length = 1,
        choices = BIKE_CHOICES,
        default = u'0',
        verbose_name = u'Bicycle Allowance'
    )
    class Meta:
        verbose_name = u'Trip'
        verbose_name_plural = u'Trips'
        ordering = ['trip_id',]
    def __unicode__(self):
        return self.trip_id


# class StopTime(models.Model): # For stop_times.txt (REQUIRED)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     class Meta:
#         verbose_name = u'Stop Time'
#         verbose_name_plural = u'Stop Times'
#         ordering = ['',]
#
#
#
#
# class FareAttribute(models.Model): # For fare_attributes.txt (OPTIONAL)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     class Meta:
#         verbose_name = u'Fare Attribute'
#         verbose_name_plural = u'Fare Attributes'
#         ordering = ['',]
#
#
# class FareRule(models.Model): # For fare_rules.txt (OPTIONAL)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     class Meta:
#         verbose_name = u'Fare Rule'
#         verbose_name_plural = u'Fare Rules'
#         ordering = ['',]
#
#
#
#
# class Frequency(models.Model): # For frequencies (OPTIONAL)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     class Meta:
#         verbose_name = u'Frequency'
#         verbose_name_plural = u'Frequencies'
#         ordering = ['',]
#
#
# class Transfer(models.Model): # For transfers.txt (OPTIONAL)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     class Meta:
#         verbose_name = u'Transfer'
#         verbose_name_plural = u'Transfers'
#         ordering = ['',]
#
#
# class FeedInfo(models.Model): # For feed_info.txt (OPTIONAL)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     class Meta:
#         verbose_name = u'Feed Info'
#         verbose_name_plural = u'Feed Info'
#         ordering = ['',]
