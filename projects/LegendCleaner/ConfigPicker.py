import yaml
import sys, os




if __name__ == "__main__":
    strBaseDir = os.path.dirname(os.path.realpath(sys.argv[0]))
    os.chdir(strBaseDir)

    with open("example.yaml", 'r') as stream:
        try:
            print(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(str(exc))