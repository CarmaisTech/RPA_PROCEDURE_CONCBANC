from datetime import datetime, time
from src.controller.controller_concbanc import main_concbanc
from src.controller.controller_libvec import main_libvec


if time(18,0) <= datetime.now().time() <= time(18,10):
    main_concbanc()

main_libvec()
