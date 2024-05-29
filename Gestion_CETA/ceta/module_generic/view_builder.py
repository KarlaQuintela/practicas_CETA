from Gestion_CETA.ceta.module_generic.views import GeneralView


def and_or_decorator(operator:function):
    def apply(builder:ViewBuilder,*args,**kwargs):
        if builder.condition is None:
            return builder.update_condition(*args,**kwargs)
        elif function.__name__ == "and_condition":
            return builder.and_condition(*args,**kwargs)
        elif function.__name__ == "or_condition":
            return builder.or_condition(*args,**kwargs)
        else:
            raise Exception("Función no reconocida")
    return apply

class ViewBuilder():

    def __init__(self,viewset: GeneralView = None,condition:function=None):
        self.viewset = viewset
        self.condition = condition

    def update_condition(self,condition:function):
        #returns a ViewBuilder
        self.condition = condition
        return self

    def add_viewset(self,viewset: GeneralView,condition:function=None):
        self.viewset = viewset
        if condition is not None:
            self.update_condition(condition)
        return self

    def clear_viewset(self)->None:
        self.viewset,self.condition = None

    @and_or_decorator
    def and_condition(self,condition:function):
        #returns a ViewBuilder
        return self.update_condition(lambda _: self.condition() and condition())
    
    @and_or_decorator
    def or_condition(self,condition:function):
        #returns a ViewBuilder
        return self.update_condition(lambda _: self.condition() or condition())
    
    def buildQuery(self)->GeneralView:
        view = self.viewset()
        view.queryset = view.model.objects.filter(self.condition)
        self.clear_viewset()
        return view
