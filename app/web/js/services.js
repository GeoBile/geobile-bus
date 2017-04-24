'use strict';

/* Services */

var services = angular.module('geobile.services', ['ngResource']);

services.factory('get_bus_stops', function ($resource) {
    return $resource('/api/v1/stops', {}, {
        query: {
            method: 'GET',
            params: {},
            isArray: false
        }
    })
});
