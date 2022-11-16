import 'react-big-calendar/lib/css/react-big-calendar.css';
import React from 'react';
import moment from 'moment';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import { ActivityType } from '../../../../common/types/enums/ActivityType';

const localizer = momentLocalizer(moment);

const activities = [
  {
    id: 1,
    name: 'תורנות אצל אסא',
    type: ActivityType.Asa,
    startTime: moment().month(10).day(9).hour(9),
    endTime: moment().month(10).day(9).hour(10),
    description: 'לעזור לאסא'
  }
];

const activityToEvent = ({ name, startTime, endTime }) => ({
  title: name,
  start: startTime,
  end: endTime
});

const ActivitiesCalendar = () => (
  <Calendar
    localizer={localizer}
    events={activities.map(activityToEvent)}
    startAccessor='start'
    endAccessor='end'
    style={{ height: '90%', width: '90%' }}
    rtl={true}
    views={['month']}
  />
);

export default ActivitiesCalendar;
