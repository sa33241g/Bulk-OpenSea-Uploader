import os
import dotenv
from uploader import Uploader

def main():
    # Initialize env variables
    dotenv.load_dotenv()
    seed_phrase = os.getenv("SEED_PHRASE")
    password = os.getenv("PASSWORD")

    # Initialize
    uploader = Uploader()
    uploader.connect_metamask(seed_phrase, password)

    # Connect to the specified network - ENTER THE APPROPRIATE NETWORK
    # uploader.add_network("", 0, 1) # Default network provided by Metamask
    uploader.add_network("https://rpc-mumbai.maticvigil.com/", 80001) # Custom network to add to Metamask
    uploader.open_metamask()

    # Upload to OpenSea
    uploader.connect_opensea(True)
    uploader.set_collection_url("https://testnets.opensea.io/collection/big-test-4")

    uploader.upload(os.path.join(os.getcwd(), "data", "0.svg"), "Test1")
    uploader.sign_transaction() # Only needed for the first upload
    uploader.upload(os.path.join(os.getcwd(), "data", "0.svg"), "Test2")

    # Close
    uploader.close()

# Run main if this file is run directly
if __name__ == "__main__":
    main()