---
name: gender-finder
description: Find the gender of a name
---
# Instructions
To find the gender of a name, 
first execute following shell script with name as parameter:

```bash
curl https://api.genderize.io/?name=<name>
```
Parse output in JSON format and extract value of `gender` and `probability` fields
- if `gender` is male and `probability` is greater than 0.5 print `male`
- if `gender` is male and `probability` is less than or equal to 0.5 print `female`
- if `gender` is female and `probability` is greater than 0.5 print `female`
- if `gender` is female and `probability` is less than or equal to 0.5 print `male`

