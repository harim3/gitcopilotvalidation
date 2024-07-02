<?php

//program to get facebook login page api
app.get('/auth/facebook', passport.authenticate('facebook'));

