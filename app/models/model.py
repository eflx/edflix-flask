end = 0

# this is a data-only object for holding any model data that
# comes back from the API
class Model(object):
    def __init__(self, **params):
        for param in params:
            # set each param as an attribute on the model
            # so we can refer to it after as, e.g., user.name,
            # etc.
            setattr(self, param, params[param])
        end
    end
end
