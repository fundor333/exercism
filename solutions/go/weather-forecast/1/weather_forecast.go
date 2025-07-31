// Package weather 
// provide the forcast for a city.
package weather

// CurrentCondition
// rapresent the weather current condition.
var CurrentCondition string

// CurrentLocation
// rapresent the current location of the query.
var CurrentLocation string

// Forecast
// return the forecast of the location.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
