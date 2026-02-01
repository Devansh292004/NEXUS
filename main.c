/* Generated C Code */
#include <stdio.h>


#include <openssl/sha.h>
#include <string.h>
#include <stdio.h>

void compute_sha256(const char *str, char outputBuffer[65]) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, str, strlen(str));
    SHA256_Final(hash, &sha256);
    int i = 0;
    for(i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        snprintf(outputBuffer + (i * 2), 3, "%02x", hash[i]);
    }
    outputBuffer[64] = 0;
}


int main() {
    printf("NEXUS generated application running.\n");
    return 0;
}
