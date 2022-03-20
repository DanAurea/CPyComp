#define RESERVED_ARRAY_LEN 480U
#define RESERVED2_ARRAY_LEN 12U

// Provided as example for FAT32 partition structure
#define NUMBER_FAT 12
#define SECTOR_PER_FAT 4
#define FAT_REGION_SIZE NUMBER_FAT * SECTOR_PER_FAT

#define NUMBER_ROOT_ENTRIES 24
#define BYTES_PER_SEC 64
#define ROOT_DIR_SIZE NUMBER_ROOT_ENTRIES * BYTES_PER_SEC

#define NUMBER_CLUSTER 128
#define SECTOR_PER_CLUSTER 4
#define DATA_SIZE NUMBER_CLUSTER * SECTOR_PER_CLUSTER