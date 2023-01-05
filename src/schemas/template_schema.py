TEMPLATE_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://github.com/Udayraj123/OMRChecker/tree/master/src/schemas/template-schema.json",
    "title": "Template Validation Schema",
    "description": "OMRChecker input template schema",
    "type": "object",
    "required": [
        "dimensions",
        "bubbleDimensions",
        "concatenations",
        "singles",
        "preProcessors",
    ],
    "properties": {
        "dimensions": {
            "description": "The dimensions to which each input image will be resized to before processing",
            "type": "array",
            "items": {"type": "integer"},
            "minItems": 2,
            "maxItems": 2,
        },
        "bubbleDimensions": {
            "description": "The dimensions of the overlay bubble area",
            "type": "array",
            "items": {"type": "integer"},
            "minItems": 2,
            "maxItems": 2,
        },
        "preProcessors": {
            "description": "Custom configuration values to use in the template's directory",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "enum": [
                            "CropOnMarkers",
                            "CropPage",
                            "FeatureBasedAlignment",
                            "ReadBarcode",
                            "GaussianBlur",
                            "Levels",
                            "MedianBlur",
                        ],
                        "type": "string",
                    },
                    "options": {"type": "object"},
                },
                "required": ["name", "options"],
                "allOf": [
                    {
                        "if": {"properties": {"name": {"const": "CropOnMarkers"}}},
                        "then": {
                            "properties": {
                                "options": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "properties": {
                                        "relativePath": {"type": "string"},
                                        "min_matching_threshold": {"type": "number"},
                                        "max_matching_variation": {"type": "number"},
                                        "marker_rescale_range": {
                                            "type": "array",
                                            "prefixItems": [
                                                {"type": "integer"},
                                                {"type": "integer"},
                                            ],
                                            "maxItems": 2,
                                            "minItems": 2,
                                        },
                                        "marker_rescale_steps": {"type": "integer"},
                                        "apply_erode_subtract": {"type": "boolean"},
                                        "sheetToMarkerWidthRatio": {"type": "number"},
                                    },
                                    "required": ["relativePath"],
                                }
                            }
                        },
                    },
                    {
                        "if": {
                            "properties": {"name": {"const": "FeatureBasedAlignment"}}
                        },
                        "then": {
                            "properties": {
                                "options": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "properties": {
                                        "reference": {"type": "string"},
                                        "maxFeatures": {"type": "integer"},
                                        "goodMatchPercent": {"type": "number"},
                                        "2d": {"type": "boolean"},
                                    },
                                    "required": ["reference"],
                                }
                            }
                        },
                    },
                    {
                        "if": {"properties": {"name": {"const": "Levels"}}},
                        "then": {
                            "properties": {
                                "options": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "properties": {
                                        "low": {
                                            "type": "number",
                                            "minimum": 0,
                                            "maximum": 1,
                                        },
                                        "high": {
                                            "type": "number",
                                            "minimum": 0,
                                            "maximum": 1,
                                        },
                                        "gamma": {
                                            "type": "number",
                                            "minimum": 0,
                                            "maximum": 1,
                                        },
                                    },
                                }
                            }
                        },
                    },
                    {
                        "if": {"properties": {"name": {"const": "MedianBlur"}}},
                        "then": {
                            "properties": {
                                "options": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "properties": {"kSize": {"type": "integer"}},
                                }
                            }
                        },
                    },
                    {
                        "if": {"properties": {"name": {"const": "GaussianBlur"}}},
                        "then": {
                            "properties": {
                                "options": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "properties": {
                                        "kSize": {
                                            "type": "array",
                                            "prefixItems": [
                                                {"type": "integer"},
                                                {"type": "integer"},
                                            ],
                                            "maxItems": 2,
                                            "minItems": 2,
                                        },
                                        "sigmaX": {"type": "number"},
                                    },
                                }
                            }
                        },
                    },
                    {
                        "if": {"properties": {"name": {"const": "CropPage"}}},
                        "then": {
                            "properties": {
                                "options": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "properties": {
                                        "morphKernel": {
                                            "type": "array",
                                            "prefixItems": [
                                                {"type": "integer"},
                                                {"type": "integer"},
                                            ],
                                            "maxItems": 2,
                                            "minItems": 2,
                                        }
                                    },
                                }
                            }
                        },
                    },
                ],
            },
        },
        "concatenations": {
            "description": "The Concatenations parameter is a way to tell OMRChecker which fields need to be joined together before outputting into the csv"
        },
        "singles": {
            "description": "The remaining fields(in order) whose readings shall be forwarded directly in the output csv",
            "type": "array",
            "items": {"type": "string"},
        },
        "emptyVal": {
            "description": "The value to be used in case of empty bubble detected at global level.",
            "type": "string",
        },
    },
}
