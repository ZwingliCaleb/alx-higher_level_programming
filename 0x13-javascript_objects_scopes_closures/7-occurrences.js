#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement){
	return list.filter((value)=> (value === searchElement)).length;
};
