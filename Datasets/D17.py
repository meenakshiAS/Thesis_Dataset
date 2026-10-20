def approve(self, creator):
    """
    Approve granular permission request setting a Permission entry as
    approved=True for a specific action from an user on an object instance.
    """
    self.approved = True
    self.creator = creator
    self.save()