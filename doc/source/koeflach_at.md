# Dorset Council

Support for schedules provided by [Dorset Council](https://koeflach.at), The local authority for town of Köflach.

Extracted from [Abfuhrkalender 2024](https://www.koeflach.at/fileadmin/Umwelt/Abfuhrkalender_2024.pdf)

## Configuration via configuration.yaml

```yaml
waste_collection_schedule:
    sources:
    - name: koeflach_at
      args:
        street: street
        mfh: mfh
```

### Configuration Variables

**street**
*(string) (required)*

**mfh**
*(bool) (required)*

## Example using Street

```yaml
waste_collection_schedule:
    sources:
    - name: koeflach_at
      args:
        street: "Ackerweg"
        mfh: false
```

## How to get the source argument

An easy way to receive the correct street name is to check the [PDF](https://www.koeflach.at/fileadmin/Umwelt/Abfuhrkalender_2024.pdf). Please use the exact street name and "Mehrfamilienhaus" (mfh)
