import _plotly_utils.basevalidators


class LinecolorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self,
        plotly_name='linecolor',
        parent_name='layout.ternary.aaxis',
        **kwargs
    ):
        super(LinecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='style',
            **kwargs
        )