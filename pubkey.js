//024b1f5fdd155fa387cf5438d245677c978709c83fceddc2a5ea0e69cff326a993

const bitcoinjs = require( 'bitcoinjs-lib' );

const pubkey = Buffer.from( '024b1f5fdd155fa387cf5438d245677c978709c83fceddc2a5ea0e69cff326a993', 'hex' );
const { address } = bitcoinjs.payments.p2pkh({ pubkey });
console.log( address ); // 1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs