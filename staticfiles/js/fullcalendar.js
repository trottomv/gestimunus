$(function() {
  $('#calendar').fullCalendar({
    themeSystem: 'jquery-ui',
    defaultView: 'agendaWeek',
    locale: 'it',
    firstDay: 1,
    timeFormat: 'HH:mm',
    minTime: '09:00:00',
    maxTime: '23:00:00',
    render: true,
    //height: '600',
    contentHeight: 610,
    //aspectRatio: 2,
    allDaySlot: false,
    nowIndicator: 'true',
    allDayText: '',
    googleCalendarApiKey: 'AIzaSyDudYiCO1oJoignWOwbNXjUADY8NtRdtt8',
    //    windowResize: function(view) {
    //        if ($(window).width() < 600){
    //            $('#calendar').fullCalendar( 'changeView', 'agendaDay' );
    //        } else {
    //           $('#calendar').fullCalendar( 'changeView', 'agendaWeek' );
    //        }
    //    },
    eventSources: [
      {
        googleCalendarId: '8kg534ss18tkfme2i7kchcdp60@group.calendar.google.com',
        // className: 'gcal-event' // an option!
        eventTitle: 'Siloso',
      },

      {
        googleCalendarId: 'e4p72qip88d3mcv62q5g6cfpfs@group.calendar.google.com',
        // className: 'nice-event',
        title: 'Siloso2',
      }
    ],
    eventColor: '#4b4b4b',
    views: {
      agenda: {
        // options apply to agendaWeek and agendaDay views

      },
    }
  });
});
