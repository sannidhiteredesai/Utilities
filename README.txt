This code can extract the required sections from a python dictionary ( representation of JSON/YAML ).
So, from a dictionary if following are reqiored sections: "k1.k2.k3", "k1.k4"
The result will be a dict in the following format: { "k1.k2.k3": list<values>, "k1.k4": list<values> }

Example:

For the below YAML and JSON, if the required keys are:
"section1.s1arr1item1",
"section1.s1common",
"section2.s2key1",
"section2.s2key2.commonKey"

Then the result will be:
{
	'section1.s1arr1item1': ['a1i1'],
	'section1.s1common': ['common1', 'common2'],
	'section2.s2key1': [{
		'data1': 'data1',
		'data2': 'data2'
	}],
	'section2.s2key2.commonKey': [{
		'field1': 11,
		'field2': 12
	}, {
		'field1': 21,
		'field2': 22
	}, {
		'field1': 31,
		'field2': 33
	}]
}


YAML FILE:
----------------------------------------
section1:
 - - s1arr1item1: a1i1
   - s1arr1item2: a1i2
   - s1common: common1
 - - s1arr2item1: a2i1
   - s1arr2item2: a2i2
   - s1common: common2

section2:
  - s2key1:
     data1: data1
     data2: data2
  - s2key2:
    - commonKey:
       field1: 11
       field2: 12
    - commonKey:
       field1: 21
       field2: 22
    - commonKey:
       field1: 31
       field2: 33


JSON REPRESENTATION:
----------------------------------------
{
  "section1": [
    [
      {
        "s1arr1item1": "a1i1"
      },
      {
        "s1arr1item2": "a1i2"
      },
      {
        "s1common": "common1"
      }
    ],
    [
      {
        "s1arr2item1": "a2i1"
      },
      {
        "s1arr2item2": "a2i2"
      },
      {
        "s1common": "common2"
      }
    ]
  ],
  "section2": [
    {
      "s2key1": {
        "data1": "data1",
        "data2": "data2"
      }
    },
    {
      "s2key2": [
        {
          "commonKey": {
            "field1": 11,
            "field2": 12
          }
        },
        {
          "commonKey": {
            "field1": 21,
            "field2": 22
          }
        },
        {
          "commonKey": {
            "field1": 31,
            "field2": 33
          }
        }
      ]
    }
  ]
}
----------------------------------------

