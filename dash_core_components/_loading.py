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


class Loading(DashComponent):
    """
    A Loading component that wraps any other component and displays a spinner
    until the wrapped component has rendered.
    """
    _namespace = 'dash_core_components'
    _typename = 'Loading'
    available_wildcard_properties = [

    ]
    id = ComponentProp('id', UNDEFINED, False)
    children = ComponentProp('children', UNDEFINED, False)
    type = ComponentProp('type', "'default'", False)
    fullscreen = ComponentProp('fullscreen', UNDEFINED, False)
    debug = ComponentProp('debug', UNDEFINED, False)
    className = ComponentProp('className', UNDEFINED, False)
    style = ComponentProp('style', UNDEFINED, False)
    color = ComponentProp('color', '#119DFF', False)
    loading_state = ComponentProp('loading_state', UNDEFINED, False)

    def __init__(
        self,
        children=UNDEFINED,
        id=UNDEFINED,
        type="'default'",
        fullscreen=UNDEFINED,
        debug=UNDEFINED,
        className=UNDEFINED,
        style=UNDEFINED,
        color='#119DFF',
        loading_state=UNDEFINED,
        **kwargs
    ):
        # type: (typing.Union[typing.Union[typing.List[typing.Union[str, int, float, DashComponent,typing.List[typing.Union[str, int, float, DashComponent]]]],typing.Union[str, int, float, DashComponent,typing.List[typing.Union[str, int, float, DashComponent]]]], Undefined], typing.Union[str, Undefined], typing.Union[typing.Any, Undefined], typing.Union[bool, Undefined], typing.Union[bool, Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict, Undefined], typing.Union[str, Undefined], typing.Union[typing.Dict[str, typing.Union[bool, str]], Undefined], typing.Any) -> None # noqa: E501
        """
        :param id:
        :param children: Array that holds components to render
        :param type: Property that determines which spinner to show - one
            of 'graph', 'cube', 'circle', 'dot', or 'default'.
            (Possible values: 'graph', 'cube', 'circle', 'dot',
            'default')
        :param fullscreen: Boolean that determines if the loading spinner
            will be displayed full-screen or not
        :param debug: Boolean that determines if the loading spinner will
            display the status.prop_name and component_name
        :param className: Additional CSS class for the root DOM node
        :param style: Additional CSS styling for the root DOM node
        :param color: Primary colour used for the loading spinners
        :param loading_state: Object that holds the loading state object
            coming from dash-renderer
        """
        kws = {
            k: v for k, v in locals().items() if k not in ('self', 'kwargs')
        }
        kws.update(kwargs)
        DashComponent.__init__(self, **kws)
