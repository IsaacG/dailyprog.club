import { ed25519 } from "@noble/curves/ed25519.js";
import { mnemonicToEntropy, validateMnemonic } from "@scure/bip39";
import { wordlist } from "@scure/bip39/wordlists/english.js";
import * as fs from "node:fs/promises";
import * as path from "node:path";
import { encodePublicKey, toBase64Url } from "../lib/identity-protocol.ts";

/**
 * Derives an Ed25519 keypair from a 24-word BIP39 mnemonic and saves it to a JSON file.
 *
 * @param {string} mnemonic - 24-word BIP39 recovery phrase
 * @param {string} outputPath - Path to output file
 */
export async function saveKeypairFromMnemonic(mnemonic, outputPath) {
  const normalized = mnemonic.trim().replace(/\s+/g, " ").toLowerCase();
  if (!validateMnemonic(normalized, wordlist)) {
    throw new Error("Invalid BIP39 24-word recovery phrase.");
  }

  // Extract 32 bytes of seed entropy
  const seed = mnemonicToEntropy(normalized, wordlist);

  // Derive Ed25519 public key bytes
  const publicKeyBytes = ed25519.getPublicKey(seed);
  const publicKeyString = encodePublicKey("ed25519", publicKeyBytes);

  const keypairData = {
    alg: "ed25519",
    publicKey: publicKeyString,
    rawPublicKey: toBase64Url(publicKeyBytes),
    rawPrivateKey: toBase64Url(seed),
    createdAt: new Date().toISOString(),
  };

  const fullPath = path.resolve(outputPath);
  await fs.mkdir(path.dirname(fullPath), { recursive: true });
  await fs.writeFile(fullPath, JSON.stringify(keypairData, null, 2), "utf-8");

  console.log(`Keypair successfully saved to: ${fullPath}`);
  console.log(`Public Key Identity: ${publicKeyString}`);
  return keypairData;
}

// CLI Execution Handler
const args = process.argv.slice(2);
if (args.length > 0) {
  const mnemonicArg = args[0];
  const outputFileArg = args[1] || "./keypair.json";

  saveKeypairFromMnemonic(mnemonicArg, outputFileArg).catch((err) => {
    console.error("Error generating keypair:", err.message);
    process.exit(1);
  });
}
