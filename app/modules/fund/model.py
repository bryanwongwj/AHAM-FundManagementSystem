import marshmallow as ma

class FundSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True,
                       metadata={"example": 1})
    name = ma.fields.String(validate=ma.validate.Length(max=50),
                            metadata={"example": "AHAM Enhanced Deposit Fund"},
                            required=True)
    
class FundUpdateSchema(ma.Schema):
    performance = ma.fields.Float(metadata={"example": 183.644138},
                                  required=True)

class FundDetailSchema(FundUpdateSchema, FundSchema): 
    fund_manager_name = ma.fields.String(validate=ma.validate.Length(max=50),
                                         metadata={"example": "johndoe"},
                                         required=True)
    dscp = ma.fields.String(validate=ma.validate.Length(max=200),
                            metadata={"example": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."})
    dt_create = ma.fields.String(dump_only=True,
                                 metadata={"example": "2024-11-09 08:57:31"})
    nav = ma.fields.Float(metadata={"example": 1.2253},
                          required=True)
    
