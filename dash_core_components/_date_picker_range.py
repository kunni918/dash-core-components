"""
Autogenerated file
DO NOT EDIT.
CONTENT WILL BE OVERWRITTEN!

WARNING: Do not import this file directly!
"""
import typing

from dash_component_system import (
    DashComponent, UNDEFINED, Undefined, ComponentProp
)


class DatePickerRange(DashComponent):
    """
    DatePickerRange is a tailor made component designed for selecting timespan
    across multiple days off of a calendar.  The DatePicker integrates well
    with the Python datetime module with the startDate and endDate being
    returned in a string format suitable for creating datetime objects.  This
    component is based off of Airbnb's react-dates react component which can
    be found here: https://github.com/airbnb/react-dates
    """
    _namespace = 'dash_core_components'
    _typename = 'DatePickerRange'
    available_wildcard_properties = [

    ]
    id = ComponentProp('id', UNDEFINED, False)
    start_date = ComponentProp('start_date', UNDEFINED, False)
    end_date = ComponentProp('end_date', UNDEFINED, False)
    min_date_allowed = ComponentProp('min_date_allowed', UNDEFINED, False)
    max_date_allowed = ComponentProp('max_date_allowed', UNDEFINED, False)
    initial_visible_month = ComponentProp('initial_visible_month', UNDEFINED, False)
    start_date_placeholder_text = ComponentProp('start_date_placeholder_text', UNDEFINED, False)
    end_date_placeholder_text = ComponentProp('end_date_placeholder_text', UNDEFINED, False)
    day_size = ComponentProp('day_size', 39, False)
    calendar_orientation = ComponentProp('calendar_orientation', "'horizontal'", False)
    is_RTL = ComponentProp('is_RTL', False, False)
    reopen_calendar_on_clear = ComponentProp('reopen_calendar_on_clear', False, False)
    number_of_months_shown = ComponentProp('number_of_months_shown', 1, False)
    with_portal = ComponentProp('with_portal', False, False)
    with_full_screen_portal = ComponentProp('with_full_screen_portal', False, False)
    first_day_of_week = ComponentProp('first_day_of_week', "0", False)
    minimum_nights = ComponentProp('minimum_nights', UNDEFINED, False)
    stay_open_on_select = ComponentProp('stay_open_on_select', False, False)
    show_outside_days = ComponentProp('show_outside_days', UNDEFINED, False)
    month_format = ComponentProp('month_format', UNDEFINED, False)
    display_format = ComponentProp('display_format', UNDEFINED, False)
    disabled = ComponentProp('disabled', False, False)
    clearable = ComponentProp('clearable', False, False)
    style = ComponentProp('style', UNDEFINED, False)
    className = ComponentProp('className', UNDEFINED, False)
    updatemode = ComponentProp('updatemode', "'singledate'", False)
    loading_state = ComponentProp('loading_state', UNDEFINED, False)

    def __init__(
        self,
        id=UNDEFINED,
        start_date=UNDEFINED,
        end_date=UNDEFINED,
        min_date_allowed=UNDEFINED,
        max_date_allowed=UNDEFINED,
        initial_visible_month=UNDEFINED,
        start_date_placeholder_text=UNDEFINED,
        end_date_placeholder_text=UNDEFINED,
        day_size=39,
        calendar_orientation="'horizontal'",
        is_RTL=False,
        reopen_calendar_on_clear=False,
        number_of_months_shown=1,
        with_portal=False,
        with_full_screen_portal=False,
        first_day_of_week="0",
        minimum_nights=UNDEFINED,
        stay_open_on_select=False,
        show_outside_days=UNDEFINED,
        month_format=UNDEFINED,
        display_format=UNDEFINED,
        disabled=False,
        clearable=False,
        style=UNDEFINED,
        className=UNDEFINED,
        updatemode="'singledate'",
        loading_state=UNDEFINED,
        **kwargs
    ):
        # type: (typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[typing.Any, Undefined], typing.Union[bool, Undefined], typing.Union[bool, Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[bool, Undefined], typing.Union[bool, Undefined], typing.Union[typing.Any, Undefined], typing.Union[typing.Union[float, int], Undefined], typing.Union[bool, Undefined], typing.Union[bool, Undefined], typing.Union[str, Undefined], typing.Union[str, Undefined], typing.Union[bool, Undefined], typing.Union[bool, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[str, Undefined], typing.Union[typing.Any, Undefined], typing.Union[typing.Dict[str, typing.Union[bool, str]], Undefined], typing.Any) -> None # noqa: E501
        """
        :param id:
        :param start_date: Specifies the starting date for the component.
            Accepts datetime.datetime objects or strings in
            the format 'YYYY-MM-DD'
        :param end_date: Specifies the ending date for the component.
            Accepts datetime.datetime objects or strings in
            the format 'YYYY-MM-DD'
        :param min_date_allowed: Specifies the lowest selectable date for
            the component. Accepts datetime.datetime
            objects or strings in the format 'YYYY-MM-
            DD'
        :param max_date_allowed: Specifies the highest selectable date for
            the component. Accepts datetime.datetime
            objects or strings in the format 'YYYY-MM-
            DD'
        :param initial_visible_month: Specifies the month that is initially
            presented when the user opens the
            calendar. Accepts datetime.datetime
            objects or strings in the format
            'YYYY-MM-DD'
        :param start_date_placeholder_text: Text that will be displayed in
            the first input box of the date
            picker when no date is
            selected. Default value is
            'Start Date'
        :param end_date_placeholder_text: Text that will be displayed in
            the second input box of the date
            picker when no date is selected.
            Default value is 'End Date'
        :param day_size: Size of rendered calendar days, higher number
            means bigger day size and larger calendar overall
        :param calendar_orientation: Orientation of calendar, either
            vertical or horizontal. Valid options
            are 'vertical' or 'horizontal'.
            (Possible values: 'vertical',
            'horizontal')
        :param is_RTL: Determines whether the calendar and days operate
            from left to right or from right to left
        :param reopen_calendar_on_clear: If True, the calendar will
            automatically open when cleared
        :param number_of_months_shown: Number of calendar months that are
            shown when calendar is opened
        :param with_portal: If True, calendar will open in a screen overlay
            portal, not supported on vertical calendar
        :param with_full_screen_portal: If True, calendar will open in a
            full screen overlay portal, will
            take precedent over 'withPortal' if
            both are set to true, not supported
            on vertical calendar
        :param first_day_of_week: Specifies what day is the first day of
            the week, values must be from [0, ..., 6]
            with 0 denoting Sunday and 6 denoting
            Saturday (Possible values: 0, 1, 2, 3, 4,
            5, 6)
        :param minimum_nights: Specifies a minimum number of nights that
            must be selected between the startDate and
            the endDate
        :param stay_open_on_select: If True the calendar will not close
            when the user has selected a value and
            will wait until the user clicks off the
            calendar
        :param show_outside_days: If True the calendar will display days
            that rollover into the next month
        :param month_format: Specifies the format that the month will be
            displayed in the calendar, valid formats are
            variations of "MM YY". For example: "MM YY"
            renders as '05 97' for May 1997 "MMMM, YYYY"
            renders as 'May, 1997' for May 1997 "MMM, YY"
            renders as 'Sep, 97' for September 1997
        :param display_format: Specifies the format that the selected dates
            will be displayed valid formats are
            variations of "MM YY DD". For example: "MM
            YY DD" renders as '05 10 97' for May 10th
            1997 "MMMM, YY" renders as 'May, 1997' for
            May 10th 1997 "M, D, YYYY" renders as '07,
            10, 1997' for September 10th 1997 "MMMM"
            renders as 'May' for May 10 1997
        :param disabled: If True, no dates can be selected.
        :param clearable: Whether or not the dropdown is "clearable", that
            is, whether or not a small "x" appears on the
            right of the dropdown that removes the selected
            value.
        :param style: CSS styles appended to wrapper div
        :param className: Appends a CSS class to the wrapper div component.
        :param updatemode: Determines when the component should update its
            value. If `bothdates`, then the DatePicker will
            only trigger its value when the user has
            finished picking both dates. If `singledate`,
            then the DatePicker will update its value as one
            date is picked. (Possible values: 'singledate',
            'bothdates')
        :param loading_state: Object that holds the loading state object
            coming from dash-renderer
        """
        kws = {
            k: v for k, v in locals().items() if k not in ('self', 'kwargs')
        }
        kws.update(kwargs)
        DashComponent.__init__(self, **kws)
