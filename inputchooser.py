import sys
# Taken from https://bitbucket.org/maddagaska/maddautils/src/411cf3811f995de0ee6de000aed069f409afc719/__init__.py?at=master # noqa
# Offered under BSD license.

#phillip.kent@interoute.com: Added option 'include_none' (2014-11-07)
#By default, include_none=False, so a selection is required
#For an optional selection, use include_none = True 

def choose_item_from_list(items,
                          source=sys.stdin,
                          dest=sys.stdout,
                          default='-',
                          include_none = False,
                          prompt='Please select an item:'):
    # No item can be selected if there are no items
    if len(items) == 0:
        return -1

    # Use the default if we can- otherwise, make sure it's safe
    if default != '-' and (default in items or default == 'None'):
        if default == 'None':
            default = -1
        else:
            default = items.index(default)
    elif isinstance(default, int) and default in range(-1, len(items)):
        # The default is already an index in the list, or it is none
        # We don't need to do anything
        pass
    else:
        # If the default has been incorrectly set, or if it has not been set,
        # set it to nothing
        default = None

    # Ask the user to make a selection
    selection = None
    while selection is None:
        selection = default

        # Output the header
        dest.write('%s\n' % prompt)
        if include_none:
            dest.write('0. None')
            if default == -1:
                # This is the default option
                dest.write(' (default)\n')
            else:
                dest.write('\n')

        # Output all of the items
        for item in range(0, len(items)):
            dest.write('%s. %s' % (item + 1, items[item],))
            if int(item) == default:
                # This is the default option
                dest.write(' (default)\n')
            else:
                dest.write('\n')

        dest.flush()

        response = source.readline().rstrip()

        if len(response) == 0:
            # No response given, prompt again
            # Otherwise it causes a problem with 'startswith' later
            continue

        try:
            # If the input is an integer we treat it as a selection
            # We don't try to match it to the text of a list item
            response = int(response)
            response -= 1
            if response in range(-1, len(items)):
                selection = response
            else:
                # Give helpful feedback
                response += 1
                dest.write('\n')
                dest.write('I do not have an item number %s.\n' % response)
                dest.write('\n')
                dest.flush()

        except ValueError:
            # It wasn't an integer. Did it match any items in the list?
            candidates = []
            for item in ['None'] + items:
                if item.startswith(response):
                    candidates.append(item)

            # If the selection is unambiguous, accept it as the choice
            if len(candidates) == 1:
                if 'None'.startswith(response):
                    selection = -1
                else:
                    for item in items:
                        if item.startswith(response):
                            selection = items.index(item)
            elif len(candidates) > 1:
                # The response was ambiguous, it could match multiple items
                dest.write('\n')
                dest.write('%s matches multiple items. ' % response)
                dest.write('Please be more specific.\n')
                dest.write('\n')
                dest.flush()
            else:
                # The named item wasn't in our list, give useful feedback
                dest.write('\n')
                dest.write('%s is not an option.\n' % response)
                dest.write('\n')
                dest.flush()

    return selection
