from config import script_loc
import sys
if script_loc not in sys.path:
    sys.path.append(script_loc)
print(sys.path)


from chatscripts.gscript import gm_search

gm_search("capital tower singapore")


